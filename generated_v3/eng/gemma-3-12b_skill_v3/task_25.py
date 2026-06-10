from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

print("Initial cell size:", atoms.get_cell_lengths_and_angles())
print("Initial energy:", atoms.get_potential_energy())

opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

print("\nOptimized cell size:", atoms.get_cell_lengths_and_angles())
print("Optimized energy:", atoms.get_potential_energy())
