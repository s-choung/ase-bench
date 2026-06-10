from ase.spacegroup import crystal
from ase.io import write, read
a = 5.64
atoms = crystal(['Na', 'Cl'], basis=[(0,0,0), (0.5,0.5,0.5)], spacegroup=225, cellpar=[a, a, a, 90, 90, 90])
write('NaCl.cif', atoms, format='cif')
atoms_read = read('NaCl.cif')
sg_num = atoms_read.info['spacegroup']
natoms = len(atoms_read)
print(f"Spacegroup: Fm-3m ({sg_num})")
print(f"Atoms: {natoms}")
