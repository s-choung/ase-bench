from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize import BFGS

# Initialize Cu FCC bulk with initial guess lattice constant
atoms = bulk('Cu', 'fcc', a=3.5)
atoms.calc = EMT()

# Get and print pre-optimization values
initial_energy = atoms.get_potential_energy()
initial_cell = atoms.get_cell()
print("Before optimization:")
print(f"Unit cell (Å):\n{initial_cell.round(4)}")
print(f"Total energy (eV): {initial_energy:.4f}\n")

# Set up cell optimization
filter = FrechetCellFilter(atoms)
opt = BFGS(filter)
opt.run(fmax=0.01)

# Get and print post-optimization values
final_energy = atoms.get_potential_energy()
final_cell = atoms.get_cell()
print("\nAfter optimization:")
print(f"Unit cell (Å):\n{final_cell.round(4)}")
print(f"Total energy (eV): {final_energy:.4f}")
