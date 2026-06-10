from ase.build import bulk
from ase.io import write, read

atoms = bulk('Au', 'fcc', a=4.05, cubic=True)
write('au.xyz', atoms)

atoms_read = read('au.xyz')
for atom in atoms_read:
    print(f"Type: {atom.symbol}, Position: {atom.position}")
