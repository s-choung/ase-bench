from ase.build import bulk
from ase.io import write, read

atoms = bulk('Cu', 'fcc', a=3.61)
write('POSCAR', atoms, format='vasp')

atoms = read('POSCAR', format='vasp')
print(len(atoms))
print(atoms.cell)
