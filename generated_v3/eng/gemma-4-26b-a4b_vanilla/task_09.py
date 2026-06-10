from ase.build import bulk
from ase.io import write, read

# Create Cu FCC bulk structure
atoms = bulk('Cu', 'fcc', a=3.6)

# Save to POSCAR format
write('POSCAR', atoms, format='vasp')

# Read back from POSCAR
atoms_read = read('POSCAR', format='vasp')

# Print results
print(f"Number of atoms: {len(atoms_read)}")
print(f"Cell parameters (a, b, c): {atoms_read.cell.lengths()}")
