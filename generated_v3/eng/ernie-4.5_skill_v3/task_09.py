from ase import Atoms
from ase.build import bulk
from ase.io import read, write

# Create Cu FCC bulk structure
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)

# Save to POSCAR format
write('POSCAR', atoms, format='vasp')

# Read back from POSCAR
atoms_read = read('POSCAR', format='vasp')

# Print number of atoms and cell parameters
print(f"Number of atoms: {len(atoms_read)}")
print(f"Cell parameters: {atoms_read.get_cell_lengths_and_angles()}")
