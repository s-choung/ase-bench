from ase.build import bulk
from ase.io import write, read

# Create Au fcc bulk
au = bulk('Au', 'fcc', a=4.08)   # lattice constant in Å

# Save to XYZ
write('au_bulk.xyz', au)

# Read it back
au_read = read('au_bulk.xyz')

# Print symbol and Cartesian coordinates
for atom in au_read:
    print(atom.symbol, *atom.position)
