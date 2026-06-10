from ase.spacegroup import crystal

# Create NaCl crystal with spacegroup 225 (Fm-3m)
nacl = crystal(
    [('Na', (0, 0, 0)), ('Cl', (0.5, 0.5, 0.5))],
    spacegroup=225,
    cellpar=[5.64, 5.64, 5.64, 90, 90, 90]
)

# Print results
print(f"Number of atoms: {len(nacl)}")
print(f"Chemical symbols: {nacl.get_chemical_symbols()}")
