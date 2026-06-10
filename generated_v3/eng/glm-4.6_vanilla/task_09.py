from ase.build import bulk
from ase.io import read, write

cu = bulk('Cu', 'fcc', a=3.615)
write('POSCAR', cu)
cu_read = read('POSCAR')
print(f"Number of atoms: {len(cu_read)}")
print(f"Cell parameters:\n{cu_read.get_cell()}")
