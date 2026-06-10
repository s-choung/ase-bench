from ase.build import bulk
from ase.io import write, read

# create Au FCC bulk (a ≈ 4.08 Å)
au = bulk('Au', 'fcc', a=4.08)

# save to XYZ
write('au_bulk.xyz', au)

# read back
au_read = read('au_bulk.xyz')

# output types and positions
print('Symbols:', au_read.get_chemical_symbols())
print('Positions:')
for sym, pos in zip(au_read.get_chemical_symbols(),
                    au_read.get_positions()):
    print(sym, pos)
