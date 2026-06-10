from ase.collections import g2

# Retrieve CH4 from the G2 database
atoms = g2['CH4']

# Chemical formula
print('Chemical formula:', atoms.get_chemical_formula())

# Atomic coordinates (in Angstrom)
print('\nAtomic coordinates (Å):')
for sym, pos in zip(atoms.get_chemical_symbols(), atoms.get_positions()):
    print(f'{sym:2s} {pos[0]:10.6f} {pos[1]:10.6f} {pos[2]:10.6f}')

# Bond lengths (C–H)
c_idx = [i for i, s in enumerate(atoms.get_chemical_symbols()) if s == 'C'][0]
print('\nBond lengths (C–H):')
for i, s in enumerate(atoms.get_chemical_symbols()):
    if i != c_idx:
        d = atoms.get_distance(c_idx, i)
        print(f'C–{s}: {d:.4f} Å')
