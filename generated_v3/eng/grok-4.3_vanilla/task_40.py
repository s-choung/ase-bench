from ase.build import bulk
from ase.io import read, write
from ase.spacegroup import get_spacegroup
atoms = bulk('NaCl', 'rocksalt', a=5.64)
write('nacl.cif', atoms)
atoms = read('nacl.cif')
print(get_spacegroup(atoms))
print(len(atoms))
