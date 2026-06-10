from ase.build import bulk
from ase.io import write, read
from ase.spacegroup import get_spacegroup

atoms = bulk('NaCl', 'rocksalt', a=5.64)
write('nacl.cif', atoms)

atoms2 = read('nacl.cif')
sg = get_spacegroup(atoms2)

print(sg.no, sg.symbol)
print(len(atoms2))
