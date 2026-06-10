from ase import Atoms
from ase.build import carbon_nanotube

# Create a (6,6) carbon nanotube with length 4 using EMT potential
tube = carbon_nanotube((6, 6), length=4, pbc=(1, 1, 1))

# Print the number of atoms
print("Number of atoms:", len(tube))

# Print the cell information
print("Cell:", tube.cell)
