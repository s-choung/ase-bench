import ase.io
from ase.build import bulk

# Build Cu FCC bulk
cu = bulk('Cu', 'fcc', cubic=True, a=3.61)   # lattice constant a = 3.61 Å

# Save to POSCAR (VASP format)
ase.io.write('Cu_fcc_POSCAR', cu, format='vasp')

# Read the POSCAR back
cu_read = ase.io.read('Cu_fcc_POSCAR', format='vasp')

# Print information
print(f"Number of atoms: {len(cu_read)}")
print(f"Cell lengths: {cu_read.cell[0,0]}, {cu_read.cell[1,1]}, {cu_read.cell[2,2]}")
print(f"Cell angles: {cu_read.cell[0,1]}, {cu_read.cell[1,2]}, {cu_read.cell[2,0]}")
