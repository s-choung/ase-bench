from ase.build import bulk
from ase.io import write, read

atoms = bulk('Cu', 'fcc')
write('CuFCC.POSCAR', atoms, format='vasp')
atoms_read = read('CuFCC.POSCAR', format='vasp')

print(len(atoms_read))
print(atoms_read.get_cell_lengths_and_angles())
