from ase.build import bulk
from ase.io import write, read

# Cu FCC conventional cell (cubic)
cu = bulk('Cu', 'fcc', a=3.615, cubic=True)

# Write to VASP POSCAR format
write('POSCAR', cu, format='vasp')

# Read back the POSCAR
cu_read = read('POSCAR')

# Output results
print('Number of atoms:', len(cu_read))
print('Cell parameters:')
print(cu_read.get_cell())
