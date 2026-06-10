from ase.build import bulk
from ase.io import read, write

# Create Cu FCC bulk
cu = bulk('Cu', 'fcc', a=3.6)

# Save in VASP POSCAR format
write('POSCAR', cu, format='vasp')

# Read it back
cu_read = read('POSCAR', format='vasp')

# Print number of atoms and cell parameters
print(f"Number of atoms: {len(cu_read)}")
print(f"Cell parameters:\n{cu_read.cell[:]}")
print(f"Cell volume: {cu_read.cell.volume:.4f} Å³")
