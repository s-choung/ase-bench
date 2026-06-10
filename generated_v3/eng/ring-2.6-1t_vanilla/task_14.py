from ase.build import bulk

# Create NaCl in the rock‑salt (Fm‑3m) structure
atoms = bulk("NaCl", crystalstructure="rocksalt", a=5.64)

print("Number of atoms:", len(atoms))
print("Chemical symbols:", atoms.get_chemical_symbols())
