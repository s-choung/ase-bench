from ase import Atoms
from ase.build import bulk
from ase.io import write, read

# Create Cu FCC bulk structure
cu_bulk = bulk('Cu', 'fcc', a=3.6)

# Write to POSCAR file
write('POSCAR', cu_bulk)

# Read the POSCAR file back
atoms = read('POSCAR')

# Print number of atoms and cell parameters
print(atoms.get_number_of_atoms())
print(atoms.get_cell())
