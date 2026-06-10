from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase import units
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

print('Before:')
print(np.diag(atoms.get_cell())[0])
print(atoms.get_potential_energy())

opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

print('After:')
print(np.diag(atoms.get_cell())[0])
print(atoms.get_potential_energy())
