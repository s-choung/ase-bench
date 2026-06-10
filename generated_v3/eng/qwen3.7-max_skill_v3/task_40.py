from ase.build import bulk
from ase.io import write, read
from ase.spacegroup import get_spacegroup

atoms = bulk('NaCl', 'rocksalt', a=5.64)
write('NaCl.cif', atoms, format='cif')

atoms_read = read('NaCl.cif', format='cif')
sg = get_spacegroup(atoms_read)

print(f"Spacegroup: {sg}")
print(f"Number of atoms: {len(atoms_read)}")
