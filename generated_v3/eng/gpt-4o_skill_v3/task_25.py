from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize import BFGS

# Create Cu FCC bulk system
atoms = bulk('Cu', 'fcc', a=3.5)
atoms.calc = EMT()

# Print initial cell size and energy
initial_cell = atoms.get_cell_lengths_and_angles()[:3]
initial_energy = atoms.get_potential_energy()
print("Initial cell size:", initial_cell)
print("Initial energy:", initial_energy)

# Optimize using FrechetCellFilter with BFGS optimizer
filter_atoms = FrechetCellFilter(atoms)
optimizer = BFGS(filter_atoms)
optimizer.run(fmax=0.01)

# Print optimized cell size and energy
optimized_cell = atoms.get_cell_lengths_and_angles()[:3]
optimized_energy = atoms.get_potential_energy()
print("Optimized cell size:", optimized_cell)
print("Optimized energy:", optimized_energy)
