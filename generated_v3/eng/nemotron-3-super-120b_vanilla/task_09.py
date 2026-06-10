from ase.build import bulk
from ase.io import write, read

# Create Cu FCC bulk
cu = bulk('Cu', 'fcc', a=3.615)

# Write to VASP POSCAR
write('POSCAR', cu, format='vasp')

# Read back
cu_read = read('POSCAR', format='vasp')

# Output results
print('Number of atoms:', len(cu_read))
print('Cell lengths (Å):', cu_read.cell.lengths())
print('Cell angles (°):', cu_read.cell.angles())
