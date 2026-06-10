from ase.build import bulk
from ase.io import read, write
from ase.spacegroup import spacegroup

nacl = bulk('NaCl', 'rocksalt', a=5.64)
write('NaCl.cif', nacl)

nacl_read = read('NaCl.cif')
sg = spacegroup(nacl_read)

print(f"Spacegroup: {sg}")
print(f"Number of atoms: {len(nacl_read)}")
