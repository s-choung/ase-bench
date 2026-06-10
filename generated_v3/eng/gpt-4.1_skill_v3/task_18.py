from ase.collections import g2
from ase.geometry import get_distances

# Retrieve CH4 molecule
atoms = g2['CH4']

# Print atomic coordinates
print('Atomic coordinates (Å):')
for i, (sym, pos) in enumerate(zip(atoms.get_chemical_symbols(), atoms.get_positions())):
    print(f'{i:2d} {sym:2s} {pos[0]:9.4f} {pos[1]:9.4f} {pos[2]:9.4f}')

# Calculate and print C-H bond lengths
print('\nC–H bond lengths (Å):')
c_index = [i for i, s in enumerate(atoms.get_chemical_symbols()) if s == 'C'][0]
h_indices = [i for i, s in enumerate(atoms.get_chemical_symbols()) if s == 'H']
d, _ = get_distances(atoms.get_positions(), atoms.get_positions(), mic=False)
for h in h_indices:
    print(f'C({c_index})–H({h}): {d[c_index, h]:.4f}')

# Print chemical formula
print(f'\nFormula: {atoms.get_chemical_formula()}')
