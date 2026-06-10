from ase.spacegroup import crystal
from ase.io import read, write

atoms = crystal(['Na', 'Cl'],
                basis=[(0, 0, 0), (0.5, 0.5, 0.5)],
                spacegroup=225,
                cellpar=[5.64, 5.64, 5.64, 90, 90, 90],
                size=(1, 1, 1))

write('nacl.cif', atoms, format='cif')
atoms_read = read('nacl.cif', format='cif')
spacegroup_info = atoms_read.info.get('spacegroup', 'not available')
num_atoms = len(atoms_read)
print('Spacegroup:', spacegroup_info)
print('Number of atoms:', num_atoms)
