from ase import Atoms
from ase.build import molecule
from ase.visualize import view
from ase.io import write

# Create a MoS2 monolayer
mo = molecule('MoS2', kind='2H')
mo.rotate((0, 0, 0), 25)
# Print cell size
print("Cell size:", mo.get_cell_lengths_and_angles())

# Add vacuum
mo.add_vacuum(10.0)

# Print cell size again
print("Cell size after vacuum:", mo.get_cell_lengths_and_angles())

# Write the structure to a file
write('MoS2_monolayer.xyz', mo)

# Visualize the structure (optional)
# view(mo)
