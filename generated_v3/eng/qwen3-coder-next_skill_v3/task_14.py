from ase.spacegroup import crystal

# Create NaCl crystal with spacegroup 225 (Fm-3m)
nacl = crystal(['Na', 'Cl'], 
               [(0, 0, 0), (0.5, 0.5, 0.5)], 
               spacegroup=225, 
               cellpar=[5.64, 5.64, 5.64, 90, 90, 90])

# Print number of atoms and chemical symbols
print(f"Number of atoms: {len(nacl)}")
print(f"Chemical symbols: {nacl.get_chemical_symbols()}")
