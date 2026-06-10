from ase.build import bulk
from ase.io import write, read

atoms = bulk('Au', 'fcc', a=4.08, cubic=True)
write('au_fcc.xyz', atoms)

loaded = read('au_fcc.xyz')
for atom in loaded:
    print(atom.symbol, atom.position)
