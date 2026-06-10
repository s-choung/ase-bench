from ase import crystal

atoms = crystal('NaCl', basis=[(0, 0, 0), (0.5, 0.5, 0.5)], spacegroup=225, latticeconstant=5.64)
print(len(atoms))
print(atoms.get_chemical_symbols())
