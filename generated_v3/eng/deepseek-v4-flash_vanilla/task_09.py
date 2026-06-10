from ase.build import bulk
from ase.io import read, write

# Create Cu FCC bulk
cu = bulk('Cu', 'fcc', a=3.615)

# Save as VASP POSCAR
write('POSCAR', cu, format='vasp')

# Read it back
cu_read = read('POSCAR')

# Print number of atoms and cell parameters
print(len(cu_read))
print(cu_read.cell)
