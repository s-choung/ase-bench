from ase import Atoms
from ase.build import bulk
from ase.constraints import FrechetCellFilter
from ase.calculators import EMT
from ase.optimize import BFGS

# Define the Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.61)  # Initial lattice constant for Cu FCC is approx 3.61 Å
atoms.calc = EMT()  # Use Embedded-Atom Method (EAM) as the calculator for EMT

—ase defined in Atomic Simulation Environment import and initialization of the calculator.

# Print initial cell size and potential energy before optimization
initial_cell_volume = atoms.get_cell()["volume"]
initial_energy = atoms.get_potential_energy()
print("Initial cell size:", initial_cell_volume)
print("Initial potential energy:", initial_energy)

# Apply the Frechet cell filter to simultaneously optimize lattice constant and atomic positions
constraint = FrechetCellFilter(atoms)

# Optimize using BFGS with a given fmax
optimizer = BFGS()  # Initialize BFGS optimizer
optimizer.run(constraint, steps=1000, fmax=0.01)

# Print cell size and potential energy after optimization
final_cell_volume = atoms.get_cell()["volume"]
final_energy = atoms.get_potential_energy()
print("Final cell size:", final_cell_volume)
print("Final potential energy:", final_energy)
