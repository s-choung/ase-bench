from ase.build import bulk
from ase.io import write, read

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6)

# Save to VASP POSCAR format
write('POSCAR', atoms, format='vasp')

# Read it back
atoms_read = read('POSCAR', format='vasp')

# Output information
print(f"Number of atoms: {len(atoms_read)}")
print(f"Cell parameters (a, b, c, alpha, beta, gamma): {atoms_read.get_cell_lengths_and_angles()}")
