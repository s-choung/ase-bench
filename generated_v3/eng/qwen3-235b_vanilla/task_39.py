from ase import Atoms
from ase.build import bulk
from ase.io import write, read

# Create Au FCC bulk structure
au_bulk = bulk('Au', 'fcc', a=4.08)

# Write to XYZ file
write('au_bulk.xyz', au_bulk)

# Read the XYZ file back
au_bulk_read = read('au_bulk.xyz')

# Print atom types and positions
print(au_bulk_read.get_chemical_symbols())
print(au_bulk_read.get_positions())
