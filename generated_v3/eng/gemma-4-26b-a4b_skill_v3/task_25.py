import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

# Initialize Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.5)
atoms.calc = EMT()

# Record initial state
initial_energy = atoms.get_potential_energy()
initial_cell = atoms.get_cell_lengths_and_angles()[:3]

print(f"Initial Energy: {initial_energy:.4f} eV")
print(f"Initial Cell (a, b, c): {initial_cell}")

# Setup Filter and Optimizer
# FrechetCellFilter allows simultaneous relaxation of cell and positions
filter = FrechetCellFilter(atoms)
opt = BFGS(filter)

# Run optimization
opt.run(fmax=0.01)

# Record final state
final_energy = atoms.get_potential_energy()
final_cell = atoms.get_cell_lengths_and_angles()[:3]

print(f"\nFinal Energy: {final_energy:.4f} eV")
print(f"Final Cell (a, b, c): {final_cell}")
