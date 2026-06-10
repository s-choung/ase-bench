from ase import Atoms
from ase.build import bulk
from ase.io import read, write

nacl = bulk('NaCl', 'rocksalt', a=5.64)
write('NaCl.cif', nacl)
nacl_read = read('NaCl.cif')

from ase.spacegroup import get_spacegroup
spacegroup = get_spacegroup(nacl_read)
print(spacegroup)
print(len(nacl_read))
