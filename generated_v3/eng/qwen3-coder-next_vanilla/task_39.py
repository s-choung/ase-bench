from ase import Atoms
from ase.io import read, write
from ase.build import bulk

# Create Au FCC bulk
au_bulk = bulk('Au', 'fcc', a=4.08)

# Save to XYZ file
write('au_bulk.xyz', au_bulk)

# Read back from XYZ file
au_read = read('au_bulk.xyz')

# Print atom types and positions
print("Atom types:", au_read.get_chemical_symbols())
print("Positions (Angstrom):\n", au_read.get_positions())
