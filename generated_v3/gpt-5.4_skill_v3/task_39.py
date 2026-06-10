from ase.build import bulk
from ase.io import write, read

atoms = bulk('Au', 'fcc', a=4.08, cubic=True)
write('au_fcc.xyz', atoms)

atoms_read = read('au_fcc.xyz')
for atom in atoms_read:
    x, y, z = atom.position
    print(atom.symbol, x, y, z)
