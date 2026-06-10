from ase.build import bulk
from ase.io import write, read

cu_bulk = bulk('Cu', 'fcc', a=3.6)
write('POSCAR', cu_bulk, format='vasp')
read_cu_bulk = read('POSCAR')
print(len(read_cu_bulk))
print(read_cu_bulk.cell)
