from ase.build import bulk
from ase.io import read, write

# Create and save Cu FCC bulk
cu = bulk('Cu', 'fcc', a=3.6)
write('POSCAR', cu)

# Read it back
cu_read = read('POSCAR')

# Print number of atoms and cell parameters
print(f'Number of atoms: {len(cu_read)}')
print(f'Cell parameters:\n{cu_read.cell.array}')
