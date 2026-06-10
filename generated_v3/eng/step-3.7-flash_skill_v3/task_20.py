from ase.build import nanotube

# Create (6,6) carbon nanotube with 4 unit cells along the tube axis
atoms = nanotube(n=6, m=6, length=4, symbol='C')

# Print number of atoms and cell information
print(f"Number of atoms: {len(atoms)}")
print("Cell vectors (Å):\n", atoms.cell)
print("Cell lengths and angles:", atoms.get_cell_lengths_and_angles())
