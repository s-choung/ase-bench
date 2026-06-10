from ase.build import bulk
from ase.io import write, read
from ase.spacegroup import get_spacegroup

atoms = bulk('NaCl', 'rocksalt', a=5.64, cubic=True)
write('nacl.cif', atoms)

atoms2 = read('nacl.cif')
spg = get_spacegroup(atoms2)
print(spg)
print(len(atoms2))
