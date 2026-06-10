from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

# Initialize Cu FCC bulk with initial guess for lattice constant
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# Print initial state
print("Initial:")
print(f"Cell lengths: {atoms.get_cell_lengths_and_angles()[:3]} Å")
print(f"Energy: {atoms.get_potential_energy():.4f} eV")

# Setup and run optimization
opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

# Print final state
print("\nOptimized:")
print(f"Cell lengths: {atoms.get_cell_lengths_and_angles()[:3]} Å")
print(f"Energy: {atoms.get_potential_energy():.4f} eV")
