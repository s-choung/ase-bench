from ase.build import mx2

# Build MoS2 monolayer with 10 Å of vacuum along the z‑axis
atoms = mx2('MoS2', vacuum=10)

# Print the cell vectors and their lengths
print("Cell vectors (Å):")
print(atoms.cell)
print("\nCell lengths (Å):", atoms.cell.lengths())
