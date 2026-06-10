from ase.build import nanotube

atoms = nanotube(6, 6, length=4)
print(atoms.get_global_number_of_atoms())
print(atoms.cell)
