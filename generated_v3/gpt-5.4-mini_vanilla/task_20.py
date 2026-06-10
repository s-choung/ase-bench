from ase.build import nanotube

tube = nanotube(6, 6, length=4)
print("Number of atoms:", len(tube))
print("Cell:")
print(tube.cell)
