from ase.build import bulk
from ase.io import write, read

nacl = bulk('NaCl', 'rocksalt', a=5.64)
write('nacl.cif', nacl)

nacl_read = read('nacl.cif')
print(f"Spacegroup: {nacl_read.get_spacegroup()}")
print(f"Number of atoms: {len(nacl_read)}")
