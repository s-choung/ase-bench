from ase import Atoms
from ase.build import bulk
from ase.io import read, write

# Create Au FCC bulk structure
au_bulk = bulk('Au', 'fcc', a=4.08, cubic=True)

# Save to XYZ format
write('au_bulk.xyz', au_bulk)

# Read back from XYZ file
au_read = read('au_bulk.xyz')

# Print atom types and positions
print(f"Atom types: {au_read.get_chemical_symbols()}")
print("Positions (Å):")
for atom in au_read:
    print(f"  {atom.symbol}: {atom.position}")
