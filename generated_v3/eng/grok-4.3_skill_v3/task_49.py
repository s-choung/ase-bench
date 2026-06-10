import numpy as np
from ase import Atoms
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.constraints import FixAtoms
from ase.eos import EquationOfState

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()
volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 7):
    a = atoms.copy()
    a.set_cell(atoms.cell * x, scale_atoms=True)
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())
eos = EquationOfState(volumes, energies)
v0, _, _ = eos.fit()
a_eq = (v0 / 4)**(1/3)

slab = fcc111('Cu', size=(2, 2, 4), a=a_eq, vacuum=10.0)
slab.calc = EMT()
mask = [atom.tag > 2 for atom in slab]
slab.set_constraint(FixAtoms(mask=mask))
BFGS(slab).run(fmax=0.05)
print(slab.get_potential_energy())
for layer in range(1, 5):
    z_avg = np.mean([atom.z for atom in slab if atom.tag == layer])
    print(layer, z_avg)
