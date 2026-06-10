from ase.build import bulk
from ase.io import write, read

cu = bulk('Cu', 'fcc', a=3.6)
write('POSCAR', cu, format='vasp')

cu_read = read('POSCAR', format='vasp')

print(f"Number of atoms: {len(cu_read)}")
print(f"Cell lengths: {cu_read.cell.lengths()}")
print(f"Cell angles: {cu_read.cell.angles()}")
