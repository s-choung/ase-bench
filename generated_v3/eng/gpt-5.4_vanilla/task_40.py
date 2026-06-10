from ase.build import bulk
from ase.io import write, read
from ase.spacegroup import get_spacegroup

atoms = bulk('NaCl', 'rocksalt', a=5.64)

filename = 'nacl.cif'
write(filename, atoms)

atoms2 = read(filename)
sg = get_spacegroup(atoms2)

print(sg)
print(len(atoms2))
