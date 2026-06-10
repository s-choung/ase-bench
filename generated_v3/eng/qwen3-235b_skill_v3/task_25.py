from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

# Create Cu FCC bulk with initial lattice constant
atoms = bulk('Cu', 'fcc', a=3.6)

# Attach EMT calculator
atoms.calc = EMT()

# Print initial cell and energy
print(f"Initial cell: {atoms.get_cell_lengths_and_angles()[:3]}")
print(f"Initial energy: {atoms.get_potential_energy()}")

# Apply FrechetCellFilter for simultaneous cell and position optimization
filter_atoms = FrechetCellFilter(atoms)

# Set up BFGS optimizer
opt = BFGS(filter_atoms, trajectory='opt.traj')

# Run optimization
opt.run(fmax=0.01)

# Print final cell and energy
print(f"Final cell: {atoms.get_cell_lengths_and_angles()[:3]}")
print(f"Final energy: {atoms.get_potential_energy()}")
