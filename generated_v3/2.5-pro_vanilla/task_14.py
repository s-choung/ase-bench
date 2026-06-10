from ase.build import crystal

# NaCl (Fm-3m, spacegroup 225)
# Na at (0,0,0), Cl at (0.5,0.5,0.5)
# Lattice constant a = 5.64 Angstrom
nacl = crystal(['Na', 'Cl'],
               basis=[(0, 0, 0), (0.5, 0.5, 0.5)],
               spacegroup=225,
               cellpar=5.64)

# Print the number of atoms and chemical symbols
print(f"Total number of atoms: {len(nacl)}")
print(f"Chemical symbols: {nacl.get_chemical_symbols()}")
