from ase.spacegroup import crystal

# Create NaCl crystal with spacegroup 225 (Fm-3m)
nacl = crystal(
    symbols=['Na', 'Cl'],
    basis=[(0, 0, 0), (0.5, 0.5, 0.5)],
    spacegroup=225,
    cellpar=[5.64, 5.64, 5.64, 90, 90, 90]
)

# Output required values
print(f"Total number of atoms: {len(nacl)}")
print(f"Chemical symbols of all atoms: {nacl.get_chemical_symbols()}")
