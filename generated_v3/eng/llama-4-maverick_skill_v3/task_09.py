from ase import Atoms
from ase.build import bulk
from ase.io import read, write

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6)

# Save to POSCAR
write('POSCAR_Cu', atoms, format='vasp')

# Read POSCAR
atoms_read = read('POSCAR_Cu', format='vasp')

# Print info
print(f'Number of atoms: {len(atoms_read)}')
cell_lengths_and_angles = atoms_read.get_cell_lengths_and_angles()
print(f'Cell parameters: a={cell_lengths_and_angles[0]:.3f}, b={cell_lengths_and_angles[1]:.3f}, c={cell_lengths_and_angles[2]:.3f}')
print(f'Cell angles: α={cell_lengths_and_angles[3]:.2f}, β={cell_lengths_and_angles[4]:.2f}, γ={cell_lengths_and_angles[5]:.2f}')
