from ase.build import bulk
from ase.io import write, read
from ase.spacegroup import Spacegroup

nacl = bulk('NaCl', 'rocksalt', 5.64)
write('nacl.cif', nacl)

nacl2 = read('nacl.cif')
sg = Spacegroup(nacl2.get_spacegroup())
print(f"Spacegroup: {sg.symbol}({sg.no})")
print(f"Atoms: {len(nacl2)}")
