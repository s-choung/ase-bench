from ase.build import molecule

# Retrieve CH₄ from the G2 database
ch4 = molecule('CH4')

# Chemical formula
print('Formula:', ch4.get_chemical_formula())

# Atomic coordinates (Å)
print('\nAtomic coordinates:')
for i, (sym, pos) in enumerate(zip(ch4.get_chemical_symbols(),
                                   ch4.get_positions())):
    print(f'{i:2d} {sym:2s}  {pos[0]: .6f}  {pos[1]: .6f}  {pos[2]: .6f}')

# C–H bond lengths (Å)
c_idx = next(i for i, a in enumerate(ch4) if a.symbol == 'C')
h_indices = [i for i, a in enumerate(ch4) if a.symbol == 'H']
bond_lengths = [ch4.get_distance(c_idx, h, mic=False) for h in h_indices]

print('\nC–H bond lengths (Å):')
for i, d in enumerate(bond_lengths, 1):
    print(f'  C–H {i}: {d:.4f}')
