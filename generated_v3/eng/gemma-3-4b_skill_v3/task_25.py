from ase import Atoms
from ase.build import bulk
from ase.optimize import BFGS, FrechetCellFilter
from ase.calculators.emt import EMT
import numpy as np

# Create a Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# Optimize the lattice constant and atomic positions
optimizer = BFGS(FrechetCellFilter(atoms))
optimizer.run(fmax=0.01)

# Print the cell size and energy before and after optimization
print("Before optimization:")
print("Cell parameters:", atoms.get_cell_lengths_and_angles())
print("Total energy:", atoms.get_potential_energy())
print("Cell size:", atoms.get_cell()[0][0])

print("\nAfter optimization:")
print("Cell parameters:", atoms.get_cell_lengths_and_angles())
print("Total energy:", atoms.get_potential_energy())
print("Cell size:", atoms.get_cell()[0][0])
