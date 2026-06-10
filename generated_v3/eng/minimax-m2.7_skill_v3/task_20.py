from ase.build import nanotube

nt = nanotube(6, 6, length=4)
print(f"Number of atoms: {len(nt)}")
print(f"Cell:\n{nt.get_cell()}")
print(f"Cell lengths and angles: {nt.get_cell_lengths_and_angles()}")
