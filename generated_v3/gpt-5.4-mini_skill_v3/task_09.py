from ase.build import bulk
from ase.io import write, read

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
write('POSCAR', atoms, format='vasp')

atoms2 = read('POSCAR', format='vasp')
print(len(atoms2))
print(atoms2.get_cell_lengths_and_angles()[:3])
