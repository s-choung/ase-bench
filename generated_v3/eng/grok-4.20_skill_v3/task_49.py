from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.eos import EquationOfState
import numpy as np

a = 3.6
cell = bulk('Cu', 'fcc', a=a, cubic=True).get_cell()
volumes, energies = [], []
for x in np.linspace(0.94, 1.06, 9):
    atoms = bulk('Cu', 'fcc', a=a, cubic=True)
    atoms.set_cell(cell * x, scale_atoms=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a0 = (v0 * 4)** (1/3)

slab = fcc111('Cu', size=(3,3,4), a=a0, vacuum=10.0)
slab.calc = EMT()
mask = [atom.tag >= 3 for atom in slab]
slab.set_constraint(FixAtoms(mask=mask))

opt = BFGS(slab)
opt.run(fmax=0.02)

e = slab.get_potential_energy()
print('Final energy:', e)

z = slab.get_positions()[:, 2]
layers = [np.mean(z[slab.get_tags() == i]) for i in range(1, 5)]
print('Avg z per layer:', layers)
