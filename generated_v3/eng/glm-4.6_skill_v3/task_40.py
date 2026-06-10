from ase.build import bulk
from ase.io import read, write
from ase.spacegroup import get_spacegroup

atoms = bulk('NaCl', 'rocksalt', a=5.64, cubic=True)
write('NaCl.cif', atoms)

atoms = read('NaCl.cif')
print(f"Spacegroup: {get_spacegroup(atoms)}")
print(f"Number of atoms: {len(atoms)}")
