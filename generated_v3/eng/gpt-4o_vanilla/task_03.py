from ase import Atoms
from ase.build import mx2
from ase.calculators.emt import EMT

# Create a MoS2 monolayer
mos2 = mx2('MoS2', size=(1, 1, 1), vacuum=10.0)

# Set calculator
mos2.set_calculator(EMT())

# Get cell size
cell_size = mos2.get_cell()

# Print the cell size
print("Cell size (Angstrom):")
print(cell_size)
