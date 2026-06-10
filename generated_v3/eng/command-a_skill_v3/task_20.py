from ase.build import nanotube

tube = nanotube(6, 6, length=4)
print(f"Number of atoms: {len(tube)}")
print("Cell info:")
print(tube.get_cell_lengths_and_angles())
