from ase.build import bulk

# Create Ti HCP structure
atoms = bulk('Ti', 'hcp', a=2.95, c/a=1.59)

# Print cell vectors
print("Cell vectors (Å):")
for i, vec in enumerate(atoms.cell):
    print(f"  a{i+1} = {vec}")

# Print atomic positions
print("\nAtomic positions (fractional):")
for i, pos in enumerate(atoms.get_scaled_positions()):
    print(f"  Ti {i+1}: {pos}")
