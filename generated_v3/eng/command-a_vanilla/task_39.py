from ase import Atoms
from ase.io import write, read
from ase.build import bulk

# Create Au FCC bulk structure
au_bulk = bulk('Au', 'fcc', a=4.078)

# Save to XYZ file
write('Au_bulk.xyz', au_bulk)

# Read from XYZ file
au_bulk_loaded = read('Au_bulk.xyz')

# Print atom types and positions
for atom in au_bulk_loaded:
    print(f"Atom type: {atom.symbol}, Position: {atom.position}")
