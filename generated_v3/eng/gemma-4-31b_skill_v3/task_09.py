from ase.build import bulk
from ase.io import write, read

# Create Cu FCC bulk and save to POSCAR
atoms = bulk('Cu', 'fcc', a=3.61)
write('POSCAR', atoms, format='vasp')

# Read back and print information
atoms_read = read('POSCAR', format='vasp')
print(f"Number of atoms: {len(atoms_read)}")
print(f"Cell parameters: {atoms_read.get_cell_lengths_and_angles()}")
