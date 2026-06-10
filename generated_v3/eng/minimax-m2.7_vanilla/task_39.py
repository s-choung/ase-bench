from ase.build import bulk
from ase.io import write, read

# Create Au fcc bulk structure
au = bulk('Au', 'fcc', a=4.08)

# Write to XYZ format
write('au_bulk.xyz', au, format='xyz')

# Read the file back
au_read = read('au_bulk.xyz')

# Print atom types and positions
print("Atom types:", au_read.get_chemical_symbols())
print("Positions:\n", au_read.get_positions())
