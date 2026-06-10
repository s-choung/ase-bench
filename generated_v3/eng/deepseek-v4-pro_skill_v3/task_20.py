from ase.build import nanotube

# Create a (6,6) carbon nanotube with 4 unit cells along the tube axis
cnt = nanotube(6, 6, length=4)

# Print number of atoms and cell information
print(f"Number of atoms: {len(cnt)}")
print("Cell vectors (Angstrom):")
print(cnt.cell)
