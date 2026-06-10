from ase import bulk
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.eos import EquationOfState
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.5)
atoms.calc = EMT()
volumes, energies = [], []
cell = atoms.get_cell()
for x in np.linspace(0.95, 1.05, 7):
    a = atoms.copy()
    a.set_cell(cell * x, scale_atoms=True)
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())
eos = EquationOfState(volumes, energies)
a0, _, _ = eos.fit()
slab = fcc111('Cu', a=a0, size=(2, 2, 4), vacuum=10)
slab.calc = EMT()
slab.set_constraint(FixAtoms(mask=[a.tag < 2 for a in slab]))
BFGS(slab).run(fmax=0.01)
print(slab.get_potential_energy())
for layer in range(4):
    z_coords = [a.z for a in slab if a.tag == layer]
    print(layer, np.mean(z_coords))
