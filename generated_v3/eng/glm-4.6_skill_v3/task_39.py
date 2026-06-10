from ase.build import bulk
from ase.io import read, write

atoms = bulk('Au', 'fcc', a=4.08)
write('au_bulk.xyz', atoms)

atoms_read = read('au_bulk.xyz')
for atom in atoms_read:
    print(atom.symbol, atom.position)
