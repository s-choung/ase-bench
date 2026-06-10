from ase.build import bulk
from ase.io import read, write
from ase.spacegroup import get_spacegroup

nacl = bulk('NaCl', 'rocksalt', a=5.64)

write('nacl.cif', nacl)

nacl_read = read('nacl.cif')

spacegroup = get_spacegroup(nacl_read)
print(f"Spacegroup: {spacegroup}")
print(f"Number of atoms: {len(nacl_read)}")
