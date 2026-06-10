from ase.spacegroup import crystal

# Create NaCl crystal using spacegroup 225 (Fm-3m)
nacl = crystal(['Na', 'Cl'],
               basis=[(0, 0, 0), (0.5, 0.5, 0.5)],
               spacegroup=225,
               a=5.64)

# Print the number of atoms and chemical symbols
print(f"Number of atoms: {len(nacl)}")
print(f"Chemical symbols: {nacl.get_chemical_symbols()}")
