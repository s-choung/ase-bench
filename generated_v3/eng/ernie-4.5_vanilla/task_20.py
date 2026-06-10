from ase.build import nanotube
from ase.io import write

# Create a (6,6) carbon nanotube with length 4
ntube = nanotube(6, 6, length=4)

# Print the number of atoms
print("Number of atoms:", len(ntube))

# Print cell information
print("Cell dimensions:", ntube.get_cell())

# Optionally, save the structure to a file
write('nanotube.xyz', ntube)
