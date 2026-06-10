from ase.build import bulk
from ase.io import write, read

atoms = bulk('Cu', 'fcc', a=3.615)
write('POSCAR', atoms, format='vasp')

atoms2 = read('POSCAR')
cell = atoms2.cell
a = cell.lengths()[0]

print(len(atoms2))
print(a)
