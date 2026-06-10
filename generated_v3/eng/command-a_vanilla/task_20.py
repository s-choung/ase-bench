from ase.build import nanotube
from ase.io import write

# Create a (6,6) carbon nanotube with length 4
nt = nanotube(6, 6, length=4)

# Print the number of atoms
print("Number of atoms:", len(nt))

# Print the cell information
print("Cell info:\n", nt.get_cell())

# Optional: Write the structure to a file (e.g., XYZ format)
write('6_6_nanotube.xyz', nt)
