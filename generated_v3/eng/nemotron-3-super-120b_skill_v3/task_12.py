from ase.build import bulk

# lattice parameters
a = 2.95
c = a * 1.59

# create HCP Ti bulk
atoms = bulk('Ti', 'hcp', a=a, c=c, orthorhombic=False)

print("Cell vectors:")
print(atoms.get_cell())
print("\nAtomic positions (fractional):")
print(atoms.get_scaled_positions())
print("\nAtomic positions (Cartesian, Å):")
print(atoms.get_positions())
