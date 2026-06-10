from ase.build import bulk
from ase.io import read, write

atoms = bulk('Cu', 'fcc', a=3.615)
write('POSCAR', atoms, format='vasp')
atoms_read = read('POSCAR', format='vasp')
print(len(atoms_read))
print(atoms_read.get_cell_lengths_and_angles())
