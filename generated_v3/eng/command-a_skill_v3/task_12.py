from ase.build import bulk

# Create Ti HCP bulk structure with specified lattice parameters
atoms = bulk('Ti', 'hcp', a=2.95, c=2.95*1.59)

# Print cell vectors
print("Cell vectors:")
for vector in atoms.get_cell():
    print(vector)

# Print atomic positions
print("\nAtomic positions:")
for pos in atoms.get_positions():
    print(pos)
