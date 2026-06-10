from ase.build import molecule

# Load CH4 from the G2 database
atoms = molecule('CH4')

# Print atomic coordinates
print('Atomic coordinates (Å):')
for i, (sym, pos) in enumerate(zip(atoms.get_chemical_symbols(),
                                    atoms.get_positions())):
    print(f'{i:2d} {sym:2s} {pos[0]: .6f} {pos[1]: .6f} {pos[2]: .6f}')

# Compute and print C–H bond lengths
c_idx = atoms.get_chemical_symbols().index('C')
h_idxs = [i for i, s in enumerate(atoms.get_chemical_symbols()) if s == 'H']
bond_lengths = [atoms.get_distance(c_idx, h) for h in h_idxs]
print('\nC–H bond lengths (Å):', bond_lengths)

# Print chemical formula
print('\nChemical formula:', atoms.get_chemical_formula())
