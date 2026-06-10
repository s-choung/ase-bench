from ase.build import nanotube

atoms = nanotube(6, 6, 4)
print(len(atoms))
print(atoms.get_cell())
