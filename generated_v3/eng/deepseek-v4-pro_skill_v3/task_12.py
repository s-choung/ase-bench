from ase.build import bulk

# Create Ti HCP bulk with specified a and c/a ratio
a = 2.95
covera = 1.59
atoms = bulk('Ti', 'hcp', a=a, covera=covera)

print("Cell vectors (Å):")
print(atoms.get_cell())

print("\nAtomic positions (scaled coordinates):")
print(atoms.get_scaled_positions())

print("\nAtomic positions (Cartesian coordinates, Å):")
print(atoms.get_positions())
