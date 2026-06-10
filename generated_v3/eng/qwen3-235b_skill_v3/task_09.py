from ase import io
from ase.build import bulk

# Create Cu FCC bulk structure
atoms = bulk('Cu', 'fcc', a=3.6)

# Write to POSCAR file
io.write('POSCAR', atoms, format='vasp')

# Read back from POSCAR
atoms_read = io.read('POSCAR', format='vasp')

# Print number of atoms and cell parameters
print(len(atoms_read))
print(atoms_read.get_cell_lengths_and_angles())
