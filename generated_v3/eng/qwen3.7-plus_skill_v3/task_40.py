from ase.build import bulk
from ase.io import read, write
from ase.spacegroup.symmetrize import check_symmetry

atoms = bulk('NaCl', 'rocksalt', a=5.64)
write('nacl.cif', atoms)

atoms_read = read('nacl.cif')
sym = check_symmetry(atoms_read)

print(f"Spacegroup: {sym['number']} ({sym['international']})")
print(f"Number of atoms: {len(atoms_read)}")
