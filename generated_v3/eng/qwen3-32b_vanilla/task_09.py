from ase.build import bulk
from ase.io import write, read

atoms = bulk('Cu', 'fcc')
write('POSCAR', atoms, format='vasp')
atoms_read = read('POSCAR')
print(len(atoms_read))
print(atoms_read.cell.lengths())
