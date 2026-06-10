from ase.build import bulk
from ase.io import write, read

# Create a Cu FCC bulk structure and save it to a POSCAR file
cu_bulk = bulk('Cu', 'fcc', a=3.61, cubic=True)
write('POSCAR', cu_bulk, vasp5=True)

# Read the structure back from the POSCAR file
cu_read = read('POSCAR')

# Print the number of atoms
print(f"Number of atoms: {len(cu_read)}")

# Print the cell parameters
print(f"Cell parameters: {cu_read.cell.cellpar()}")
