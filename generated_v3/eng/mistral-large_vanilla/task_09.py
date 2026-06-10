from ase.build import bulk
from ase.io import write, read

cu = bulk('Cu', 'fcc', a=3.6)
write('POSCAR', cu, format='vasp')

cu_read = read('POSCAR')
print(f"Atoms: {len(cu_read)}, Cell: {cu_read.cell.cellpar()}")
