from ase.build import bulk

# Create NaCl crystal with spacegroup 225 (Fm-3m), lattice constant 5.64 Å
nacl = bulk('NaCl', 'rocksalt', a=5.64)

# Print the number of atoms and chemical symbols
print(f"Number of atoms: {nacl.numbers.size}")
print(f"Chemical symbols: {nacl.get_chemical_symbols()}")
