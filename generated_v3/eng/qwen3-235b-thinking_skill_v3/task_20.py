from ase.build import nanotube

nt = nanotube(6, 6, length=4)
print(len(nt))
print(nt.get_cell_lengths_and_angles())
