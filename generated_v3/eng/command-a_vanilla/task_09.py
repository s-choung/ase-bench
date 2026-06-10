from ase.build import bulk
from ase.io import write, read

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.61)

# Save in VASP POSCAR format
write('POSCAR', atoms, format='vasp')

# Read back from POSCAR
atoms_read = read('POSCAR', format='vasp')

# Print number of atoms and cell parameters
print(f"Number of atoms: {len(atoms_read)}")
print(f"Cell parameters: {atoms_read.cell.cellpar()}")
