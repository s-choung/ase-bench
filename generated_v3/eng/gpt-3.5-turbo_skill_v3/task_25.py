from ase.build import bulk
from ase.optimize import BFGS
from ase.constraints import FrechetCellFilter
from ase.calculators.emt import EMT

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.5)
atoms.calc = EMT()

# Print initial cell size and energy
print("Initial cell size:", atoms.get_cell_lengths_and_angles())
print("Initial energy:", atoms.get_potential_energy())

# Optimize lattice constant and atomic positions
opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

# Print final cell size and energy
print("Final cell size:", atoms.get_cell_lengths_and_angles())
print("Final energy:", atoms.get_potential_energy())
