from ase.build import bulk
from ase.io import write, read

# Create FCC bulk structure of Gold
au_bulk = bulk('Au', 'fcc', a=4.08)

# Save to XYZ format
write('au_bulk.xyz', au_bulk)

# Read it back
au_bulk_read = read('au_bulk.xyz')

# Print atom types and positions
for atom in au_bulk_read:
    print(atom.symbol, atom.position)
