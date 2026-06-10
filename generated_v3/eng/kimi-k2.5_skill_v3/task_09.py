from ase.build import bulk
from ase.io import read, write

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
write('POSCAR', atoms, format='vasp')
atoms = read('POSCAR', format='vasp')

print(len(atoms))
print(*atoms.get_cell_lengths_and_angles())
