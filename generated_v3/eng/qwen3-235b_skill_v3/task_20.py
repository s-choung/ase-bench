from ase.build import nanotube

# Create a (6,6) carbon nanotube with length=4
nt = nanotube(n=6, m=6, length=4)

# Print number of atoms and cell info
print(f"Number of atoms: {len(nt)}")
print("Cell:")
print(nt.get_cell())
print("Cell lengths and angles:", nt.get_cell_lengths_and_angles())
