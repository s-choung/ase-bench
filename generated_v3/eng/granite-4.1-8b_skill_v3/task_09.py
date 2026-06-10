from ase import Atoms
from ase.build import bulk
from ase.io import write, read

# Create Cu FCC bulk structure
atoms = bulk('Cu', 'fcc', a=3.615)

# Save to VASP POSCAR format
write('Cu_fcc.poscar', atoms, format='vasp')

# Read back the POSCAR file
atoms_read = read('Cu_fcc.poscar', format='vasp')

# Print number of atoms and cell parameters
print('Number of atoms:', len(atoms_read))
print('Cell parameters (a, b, c, alpha, beta, gamma) in Angstroms:')
print(atoms_read.get_cell_lengths_and_angles())
