from ase.build import bulk
from ase.io import write, read

cu = bulk('Cu', 'fcc', a=3.61)
write('Cu_bulk.vasp', cu, format='vasp')
cu_read = read('Cu_bulk.vasp', format='vasp')
print('Number of atoms:', len(cu_read))
print('Cell parameters:', cu_read.get_cell_lengths_and_angles())
