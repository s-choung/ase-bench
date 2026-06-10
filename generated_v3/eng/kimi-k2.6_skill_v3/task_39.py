from ase.build import bulk
from ase.io import write, read

atoms = bulk('Au', 'fcc', a=4.16, cubic=True)
write('Au_bulk.xyz', atoms)
au = read('Au_bulk.xyz')

for symbol, pos in zip(au.get_chemical_symbols(), au.get_positions()):
    print(symbol, *pos)
