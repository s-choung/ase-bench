from ase.build import nanotube

atoms = nanotube(6, 6, length=4)
print("Number of atoms:", len(atoms))
print("Cell info:")
print("Lengths:", atoms.get_cell_lengths_and_angles()[:3])
print("Angles:", atoms.get_cell_lengths_and_angles()[3:])
