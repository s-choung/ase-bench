from ase.build import bulk
from ase.io import write, read
from ase.spacegroup import get_spacegroup

nacl = bulk('NaCl', 'rocksalt', a=5.64)
write('nacl.cif', nacl)
nacl2 = read('nacl.cif')
print(get_spacegroup(nacl2))
print(len(nacl2))
