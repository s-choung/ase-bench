from ase import Atoms
from ase.build import bulk
from ase.io import read, write

# Create Au FCC bulk
atoms = bulk('Au', 'fcc', a=4.0)

# Save to XYZ file
write('au_bulk.xyz', atoms)

# Read from XYZ file
atoms_read = read('au_bulk.xyz')

# Print atom types and positions
print(atoms_read.get_chemical_symbols())
print(atoms_read.get_positions())
