from ase.build import nanotube

# (6,6) carbon nanotube with length=4 (unit cells along the axis)
tube = nanotube(n=6, m=6, length=4)

print("Number of atoms:", len(tube))
print("Unit cell (Å):")
print(tube.get_cell())
