from ase import Atoms
from ase.optimize import BFGS
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.filters import FrechetCellFilter
import numpy as np

# Initial setup
symbols = 'Cu'
a0 = 3.6  # Approximate lattice constant for Cu FCC
atoms = Atoms(symbols=symbols, cell=[a0, a0, a0], pbc=True, scaled_positions=[[0, 0, 0]])

# Attach EMT calculator
atoms.calc = EMT()

# Optional: fix some atoms to ensure proper convergence (all atoms here)
atoms.set_constraint(FixAtoms(mask=[True]*len(atoms)))

# Apply FrechetCellFilter for cell and position optimization
opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)  # Convergence criterion

# Print results before and after optimization
def print_details(atoms):
    print("Cell dimensions (Å):", np.round(atoms.cell, 3))
    print("Potential energy (eV):", np.round(atoms.get_potential_energy(), 3))

print("Before optimization:")
print_details(atoms.copy())  # Copy to show initial state
atoms.calc = EMT()  # Re-set calculator for fresh evaluation
print("\nAfter optimization:")
print_details(atoms)
