from ase.spacegroup import crystal
atoms = crystal(['Na', 'Cl'], basis=[(0,0,0), (0.5,0.5,0.5)], spacegroup=225, cellpar=5.64)
print(len(atoms))
print(''.join(atoms.get_chemical_symbols()))
