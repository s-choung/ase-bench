from ase.build import bulk
from ase.io import read, write

# Create Au FCC bulk
au_bulk = bulk('Au', 'fcc', a=4.08)
# Write to XYZ file
write('au_fcc.xyz', au_bulk)
# Read back from XYZ
au_read = read('au_fcc.xyz')
# Print atom types and positions
print(au_read.get_symbols())
print(au_read.get_positions())
