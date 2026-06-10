from ase.build import bulk
from ase.io import write, read

atoms = bulk('NaCl', 'rocksalt', a=5.64)
write('nacl.cif', atoms, format='cif')

read_atoms = read('nacl.cif', index=0)
print('Spacegroup:', read_atoms.get_spacegroup())
print('Number of atoms:', len(read_atoms))
