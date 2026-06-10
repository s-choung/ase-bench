from ase.build import nanotube

atoms = nanotube(6, 6, length=4, symbol='C')
print(len(atoms))
print(atoms.get_cell_lengths_and_angles())
