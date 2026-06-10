from ase import io
from ase.build import bulk

cu = bulk('Cu', 'fcc', a=3.615, cubic=True)
io.write('POSCAR', cu)
cu_read = io.read('POSCAR')
print(f'Number of atoms: {cu_read.get_global_info()[0]}')
print(f'Cell parameters:\n{cu_read.get_cell()}')
