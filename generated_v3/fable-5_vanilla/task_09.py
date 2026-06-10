from ase.build import bulk
from ase.io import read, write

atoms = bulk('Cu', 'fcc', a=3.615, cubic=True)
write('POSCAR', atoms, format='vasp')

atoms2 = read('POSCAR', format='vasp')
print("Number of atoms:", len(atoms2))
print("Cell parameters:")
print(atoms2.cell.cellpar())
