from ase.build import bulk
from ase.io import write, read

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.61)

# Save to POSCAR
write('Cu.poscar', atoms, format='vasp')

# Read back
atoms_read = read('Cu.poscar', format='vasp')

# Print info
print(f"Number of atoms: {len(atoms_read)}")
print(f"Cell parameters (a, b, c, alpha, beta, gamma): {atoms_read.cell.cellpar()}")
