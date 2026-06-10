from ase.spacegroup import crystal

a = 5.64
na_cl = crystal(['Na', 'Cl'],
                basis=[(0, 0, 0), (0.5, 0.5, 0.5)],
                spacegroup=225,
                cellpar=[a, a, a, 90, 90, 90])

print(len(na_cl))
print(na_cl.get_chemical_symbols())
