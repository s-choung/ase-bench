from ase.build import bulk
from ase.io import read, write

au_bulk = bulk('Au', 'fcc')
write('au_fcc.xyz', au_bulk)
au_read = read('au_fcc.xyz')

print('Atom types:', au_read.get_chemical_symbols())
print('Atom positions (Å):')
for sym, pos in zip(au_read.get_chemical_symbols(), au_read.get_positions()):
    print(f'{sym}: {pos}')
