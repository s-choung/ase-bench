from ase.build import bulk
from ase.io import read, write

au = bulk('Au', 'fcc')
write('au_bulk.xyz', au)

au_read = read('au_bulk.xyz')

for atom in au_read:
    print(f"{atom.symbol}: {atom.position}")
