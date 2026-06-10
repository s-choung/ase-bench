from ase.build import bulk

# Create a 2×2×2 Cu FCC supercell
atoms = bulk('Cu', crystalstructure='fcc', a=3.6).repeat((2, 2, 2))

# Distances from atom 0 to all other atoms (mic accounts for PBC)
distances, _ = atoms.get_distances(0, range(1, len(atoms)), mic=True)

print(f"Min distance: {distances.min():.4f} Å")
print(f"Max distance: {distances.max():.4f} Å")
