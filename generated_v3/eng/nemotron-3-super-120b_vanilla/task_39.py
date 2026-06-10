from ase import Atoms
from ase.build import bulk
from ase.io import write, read

au = bulk('Au', 'fcc', a=4.05, cubic=True)
write('au.xyz', au)
au_read = read('au.xyz')
for atom in au_read:
    print(atom.symbol, atom.position)
