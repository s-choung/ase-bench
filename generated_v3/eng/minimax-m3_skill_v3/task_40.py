from ase.io import read, write
from ase.spacegroup import crystal
from ase.build import bulk

atoms = bulk('NaCl', 'rocksalt', a=5.64)
write('NaCl.cif', atoms)

loaded = read('NaCl.cif')
sg = loaded.info.get('spacegroup')
print('Spacegroup:', sg)
print('Number of atoms:', len(loaded))
