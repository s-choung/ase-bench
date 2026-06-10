from ase.spacegroup import crystal

a = 5.64
atoms = crystal('NaCl', [(0, 0, 0), (0.5, 0.5, 0.5)], spacegroup=225,
                cellpar=[a, a, a, 90, 90, 90])

print(f'Number of atoms: {len(atoms)}')
print(f'Chemical symbols: {atoms.get_chemical_symbols()}')
