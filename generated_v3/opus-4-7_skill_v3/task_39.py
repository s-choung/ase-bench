from ase.build import bulk
from ase.io import read, write

atoms = bulk('Au', 'fcc', a=4.08, cubic=True)
write('au.xyz', atoms)

a = read('au.xyz')
for sym, pos in zip(a.get_chemical_symbols(), a.get_positions()):
    print(sym, pos)
