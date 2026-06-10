from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS, FrechetCellFilter

# Create copper Cu FCC structure
bulk_copper = Atoms('Cu', [(0.0, 0.0, 0.0)], cell=[3.62, 3.62, 3.62], pbc=True)

# Attach an EMT calculator
calc = EMT()
bulk_copper.set_calculator(calc)

# Define FrechetCellFilter
cell_filter = FrechetCellFilter(converge_to="fmax=0.01", optimizer="BFGS")

# Optimize the FCC Cu lattice constant and atomic positions using the filter
opt = BFGS(bulk_copper, filter=cell_filter)

# Print initial lattice parameter and energy
print(f"Initial cell parameter: {bulk_copper.get_cell_lengths()}")
print(f"Initial energy: {bulk_copper.calc.energy}")

# Run the optimization
opt.run(fmax=0.01)

# Print final lattice parameter and energy
print(f"Final cell parameter: {bulk_copper.get_cell_lengths()}")
print(f"Final energy: {bulk_copper.calc.energy}")
