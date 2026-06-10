from ase.lattice import bulk
from ase.io import write, read

# Create Cu FCC bulk
cu = bulk('Cu', 'fcc', a=3.61)

# Save to POSCAR
write('POSCAR', cu, format='vasp')

# Read it back
cu_read = read('POSCAR', format='vasp')

# Print number of atoms and cell parameters
print(f"Number of atoms: {len(cu_read)}")
print(f"Cell parameters: {cu_read.cell.lengths()}")
