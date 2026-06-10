from ase.build import nanotube
atoms = nanotube(6, 6, length=4)
print(len(atoms), atoms.cell)
