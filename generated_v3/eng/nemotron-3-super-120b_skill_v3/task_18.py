from ase.build import molecule
from ase import Atoms

# Retrieve CH4 from G2 database
mol = molecule('CH4')

# Chemical formula
print('Formula:', mol.get_chemical_formula())

# Atomic coordinates
print('Coordinates (Å):')
for i, (sym, pos) in enumerate(zip(mol.get_chemical_symbols(), mol.get_positions())):
    print(f'{i}: {sym} {pos}')

# C-H bond lengths
C_idx = mol.get_chemical_symbols().index('C')
H_idxs = [i for i, sym in enumerate(mol.get_chemical_symbols()) if sym == 'H']
print('C-H bond lengths (Å):')
for h in H_idxs:
    d = mol.get_distance(C_idx, h)
    print(f'H{h}: {d:.4f}')
