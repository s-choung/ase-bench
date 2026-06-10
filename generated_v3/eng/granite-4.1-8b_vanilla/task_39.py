from ase import Atoms
from ase.build import bulk

# Create Au FCC bulk structure
gold = bulk('Au', 'fcc', a=4.078)

# Save to an XYZ file
gold.write('gold_fcc.xyz')

# Read the file back
gold_read = Atoms(read='gold_fcc.xyz')

# Print atom types and positions
for atom in gold_read:
    print(atom.symbol, atom.position)
