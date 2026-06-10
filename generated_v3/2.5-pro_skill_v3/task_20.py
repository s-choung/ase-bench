from ase.build import nanotube

# Create a (6,6) carbon nanotube with length=4
cnt = nanotube(6, 6, length=4, symbol='C')

# Print the number of atoms and cell information
print(f"Number of atoms: {len(cnt)}")
print("Cell information:")
print(cnt.cell)
