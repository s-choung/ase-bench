from ase.build import bulk
from ase.io import read, write

atoms = bulk('Cu', 'fcc', cubic=True)
write('POSCAR', atoms, format='vasp')
atoms = read('POSCAR', format='vasp')
print(len(atoms))
print(atoms.cell)
