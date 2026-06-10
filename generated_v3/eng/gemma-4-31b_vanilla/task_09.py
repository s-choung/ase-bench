from ase.build import bulk
from ase.io import write, read

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.61)

# Save to POSCAR format
write('POSCAR', atoms, format='vasp')

# Read back from POSCAR
atoms_read = read('POSCAR')

# Print results
print(f"Number of atoms: {len(atoms_read)}")
print(f"Cell parameters:\n{atoms_read.get_cell()}")
