from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

# Initialize Cu FCC bulk structure
atoms = bulk('Cu', 'fcc', a=3.5, cubic=True)
atoms.calc = EMT()

# Print pre-optimization values
print("=== Before Optimization ===")
print(f"Unit cell (Å):\n{atoms.get_cell()}")
print(f"Total potential energy (eV): {atoms.get_potential_energy():.4f}\n")

# Set up cell + position relaxation
relax_filter = FrechetCellFilter(atoms)
optimizer = BFGS(relax_filter)
optimizer.run(fmax=0.01)

# Print post-optimization values
print("\n=== After Optimization ===")
print(f"Unit cell (Å):\n{atoms.get_cell()}")
print(f"Total potential energy (eV): {atoms.get_potential_energy():.4f}")
