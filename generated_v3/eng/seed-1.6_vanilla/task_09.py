from ase.build import bulk
from ase.io import read, write

cu = bulk('Cu', 'fcc')
write('POSCAR', cu, format='vasp')
cu_read = read('POSCAR')
print(f'Number of atoms: {cu_read.get_number_of_atoms()}')
print(f'Cell parameters (Å):\n{cu_read.get_cell()}')
