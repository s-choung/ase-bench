from ase.build import nanotube

atoms = nanotube(6, 6, layers=3, bond=4/3)
print(len(atoms))
print(atoms.get_cell())
