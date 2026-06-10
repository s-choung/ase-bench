from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FrechetCellFilter
import numpy as np

# Create Cu FCC bulk
cu = bulk('Cu', 'fcc', a=3.6)

# Assign EMT calculator
cu.calc = EMT()

# Print initial cell and energy
print(f"Initial cell vectors:\n{cu.cell}")
print(f"Initial energy: {cu.get_potential_energy():.4f} eV")

# Apply FrechetCellCompletion to optimize cell and positions
fcf = FrechetCellFilter(cu)

# Optimize with BFGS
opt = BFGS(fcf, fmax=0.01)
opt.run()

# Print final cell and energy
print(f"Final cell vectors:\n{cu.cell}")
print(f"Final energy: {cu.get_potential_energy():.4f} eV")
