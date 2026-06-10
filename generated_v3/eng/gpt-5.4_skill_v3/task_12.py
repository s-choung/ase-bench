from ase.build import bulk

a = 2.95
c_over_a = 1.59
atoms = bulk('Ti', 'hcp', a=a, c=a * c_over_a)

print('Cell vectors (Angstrom):')
for v in atoms.get_cell():
    print(f'{v[0]:10.6f} {v[1]:10.6f} {v[2]:10.6f}')

print('\nAtomic positions (Angstrom):')
for i, (sym, pos) in enumerate(zip(atoms.get_chemical_symbols(), atoms.get_positions())):
    print(f'{i:3d} {sym:2s} {pos[0]:10.6f} {pos[1]:10.6f} {pos[2]:10.6f}')
