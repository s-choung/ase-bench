from ase.spacegroup import crystal
atoms = crystal('NaCl', [(0,0,0), (0.5,0.5,0.5)], spacegroup=225, lattice_parameters=(5.64,5.64,5.64))
print(len(atoms))
print(atoms.get_chemical_symbols())
