from ase import Atoms
from ase.build import bulk
from ase.io import write, read

# Create Cu FCC bulk and save in VASP POSCAR format
atoms = bulk('Cu', 'fcc', a=3.5)
write('Cu_fcc_bulk.POSCAR', atoms, format='vasp')

# Read back the saved POSCAR file
atoms_read = read('Cu_fcc_bulk.POSCAR', format='vasp')

# Print the number of atoms and cell parameters of the read structure
print(f"Number of atoms: {len(atoms_read)}")
cell_params = atoms_read.get_cell_lengths_and_angles()
print(f"Cell parameters: a={cell_params[0]}, b={cell_params[1]}, c={cell_params[2]}")
