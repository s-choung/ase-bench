from ase.spacegroup import crystal

a = 5.64  # Å
atoms = crystal(['Na', 'Cl'],
                basis=[(0, 0, 0), (0.5, 0.5, 0.5)],
                spacegroup=225,
                cellpar=[a, a, a, 90, 90, 90])

print(atoms.get_number_of_atoms())
print(atoms.get_chemical_symbols())
