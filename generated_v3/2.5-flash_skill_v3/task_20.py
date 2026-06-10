from ase.build import nanotube

# (6,6) carbon nanotube with length=4
atoms = nanotube(6, 6, length=4, symbol='C')

# Print number of atoms
print(f"Number of atoms: {len(atoms)}")

# Print cell information
print("Cell:")
print(atoms.get_cell())
