from ase.build import bulk
from ase.io import read, write

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc')

# Save to VASP POSCAR format
write('POSCAR', atoms, format='vasp')

# Read back from POSCAR
read_atoms = read('POSCAR', format='vasp')

# Print number of atoms and cell parameters
print(f"Number of atoms: {len(read_atoms)}")
print(f"Cell parameters [a, b, c, alpha, beta, gamma]: {read_atoms.get_cell_lengths_and_angles()}")
