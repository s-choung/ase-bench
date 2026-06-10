from ase import Atoms
from ase.build import nanotube
from ase.visualize import view

# Create a (6,6) carbon nanotube with length=4
tube = nanotube(6, 6, length=4)

# Print the number of atoms
print(f"Number of atoms: {len(tube)}")

# Print the cell information
print(f"Cell dimensions: {tube.get_cell()[0]} {tube.get_cell()[1]} {tube.get_cell()[2]}")
# Optionally visualize the nanotube
# view(tube)
