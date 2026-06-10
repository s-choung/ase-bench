from ase.build import nanotube

atoms = nanotube(6, 6, length=4)

print(len(atoms))
print(atoms.cell)
print(atoms.get_cell_lengths_and_angles())
