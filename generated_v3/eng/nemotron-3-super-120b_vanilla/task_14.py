from ase.build import bulk

# Create NaCl rock‑salt structure (space group 225) with a = 5.64 Å
atoms = bulk('NaCl', crystalstructure='rocksalt', a=5.64)

# Print number of atoms and chemical symbols
print(len(atoms))
print(atoms.get_chemical_symbols())
