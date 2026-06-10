from ase.spacegroup import crystal

atoms = crystal(['Na', 'Cl'], [(0, 0, 0), (0.5, 0.5, 0.5)],
                spacegroup=225, cell=5.64)
print(len(atoms), atoms.get_chemical_symbols())
