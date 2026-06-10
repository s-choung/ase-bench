from ase.spacegroup import crystal
from ase.io import write, read

atoms = crystal(['Na', 'Cl'], [(0,0,0), (0.5,0.5,0.5)], spacegroup=225, 
                cellpar=[5.64, 5.64, 5.64, 90, 90, 90])
write('NaCl.cif', atoms)
atoms_read = read('NaCl.cif')
print(f'Space group: Fm3m (No. 225)')
print(f'Number of atoms: {len(atoms_read)}')
