from ase.build import bulk
from ase.io import read, write

# Create a Cu FCC bulk structure
cu_bulk = bulk('Cu', 'fcc', a=3.6)

# Save the structure in VASP POSCAR format
write('POSCAR', cu_bulk, format='vasp')

# Read the structure back
cu_bulk_read = read('POSCAR', format='vasp')

# Print the number of atoms and cell parameters
print("Number of atoms:", len(cu_bulk_read))
print("Cell parameters:", cu_bulk_read.cell)
