from ase import Atoms
from ase.build import bulk
from ase.io import write, read

# Create Au FCC bulk structure
atoms = bulk('Au', 'fcc', a=4.08)

# Write to XYZ file
write('au_bulk.xyz', atoms)

# Read back from XYZ file
atoms_read = read('au_bulk.xyz')

# Print atom types and positions
print(atoms_read.get_chemical_symbols())
print(atoms_read.get_positions())
