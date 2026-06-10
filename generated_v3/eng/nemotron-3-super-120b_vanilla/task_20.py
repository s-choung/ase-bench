from ase.build import nanotube

# Create a (6,6) carbon nanotube with 4 unit cells along the axis
tube = nanotube(6, 6, length=4)

# Output the requested information
print("Number of atoms:", len(tube))
print("Cell vectors:\n", tube.cell)
