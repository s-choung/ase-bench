from ase.build import nanotube

atoms = nanotube(6, 6, length=4, symbol='C')

print("Number of atoms:", len(atoms))
print("Cell:")
print(atoms.cell)
print("Cell lengths and angles:", atoms.get_cell_lengths_and_angles())
