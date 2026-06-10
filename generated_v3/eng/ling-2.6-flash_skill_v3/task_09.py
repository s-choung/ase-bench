from ase import Atoms
from ase.build import bulk
from ase.io import write, read

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6)

# Save in VASP POSCAR format
write('POSCAR', atoms, format='vasp')

# Read back
atoms_read = read('POSCAR')

# Output
print(f'Number of atoms: {len(atoms_read)}')
print(f'Cell parameters: {atoms_read.cell.get_lengths_and_angles()}')
