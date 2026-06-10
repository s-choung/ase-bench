from ase.build import bulk
from ase.io import read, write

atoms = bulk('Au', 'fcc', a=4.08)
write('au_fcc.xyz', atoms)

loaded = read('au_fcc.xyz')
print('Atom types:', loaded.get_chemical_symbols())
print('Positions:', loaded.get_positions())
