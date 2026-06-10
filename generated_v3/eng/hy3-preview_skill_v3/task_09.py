from ase.build import bulk
from ase.io import read, write

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6)

# Save in VASP POSCAR format
write('POSCAR', atoms, format='vasp')

# Read back
atoms_read = read('POSCAR', format='vasp')

# Print results
print(f"Number of atoms: {len(atoms_read)}")
print(f"Cell parameters (Å, degrees): {atoms_read.get_cell_lengths_and_angles()}")
