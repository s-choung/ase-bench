from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
import numpy as np

atoms = bulk('Cu','fcc',a=3.5)
atoms.calc = EMT()

print("Initial cell size:", atoms.get_cell())
print("Initial energy:", atoms.get_potential_energy())

opt = BFGS(FrechetCellFilter(atoms), trajectory='cu_optimization.traj')
opt.run(fmax=0.01)

print("Final cell size:", atoms.get_cell())
print("Final energy:", atoms.get_potential_energy())
