from ase.build import bulk
from ase.io import read, write

atoms = bulk('Au', 'fcc', a=4.08)
write('Au_bulk.xyz', atoms)
loaded_atoms = read('Au_bulk.xyz')

for atom in loaded_atoms:
    print(atom.symbol, atom.position)
