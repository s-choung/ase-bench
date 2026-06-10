from ase.build import bulk

# Create Ti HCP bulk structure
a = 2.95
c_over_a = 1.59
c = a * c_over_a
atoms = bulk('Ti', crystalstructure='hcp', a=a, c=c)

# Print cell vectors and atomic positions
print("Cell vectors:")
print(atoms.cell)
print("\nAtomic positions:")
print(atoms.get_positions())
