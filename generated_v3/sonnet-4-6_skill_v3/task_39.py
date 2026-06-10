from ase.build import bulk
from ase.io import read, write

atoms = bulk('Au', 'fcc', a=4.08, cubic=True)
write('au_bulk.xyz', atoms)

atoms_read = read('au_bulk.xyz')
for atom in atoms_read:
    print(f"{atom.symbol}  {atom.position[0]:.4f}  {atom.position[1]:.4f}  {atom.position[2]:.4f}")
