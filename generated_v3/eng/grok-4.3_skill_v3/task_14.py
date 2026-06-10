from ase.spacegroup import crystal
atoms = crystal(['Na','Cl'], [(0,0,0),(0.5,0.5,0.5)], 225, cellpar=[5.64]*3+[90]*3)
print(len(atoms), atoms.get_chemical_symbols())
