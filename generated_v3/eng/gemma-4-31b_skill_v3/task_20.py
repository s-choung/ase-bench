from ase.build import nanotube

# Create (6,6) carbon nanotube
cnt = nanotube(6, 6, length=4, symbol='C')

# Print atoms count and cell details
print(f"Number of atoms: {len(cnt)}")
print(f"Cell: {cnt.get_cell()}")
print(f"Cell lengths and angles: {cnt.get_cell_lengths_and_angles()}")
