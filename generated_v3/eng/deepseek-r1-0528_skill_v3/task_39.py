from ase.build import bulk
from ase.io import read, write

atoms = bulk('Au', 'fcc', a=4.08)
write('au_fcc.xyz', atoms)
restored_atoms = read('au_fcc.xyz')

for i, atom in enumerate(restored_atoms):
    symbol = atom.symbol
    position = atom.position
    print(f"Atom {i}: {symbol} {position}")
