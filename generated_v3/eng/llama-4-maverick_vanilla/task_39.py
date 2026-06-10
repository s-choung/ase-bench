from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.io import read, write

# Create Au FCC bulk
au_bulk = bulk('Au', 'fcc', a=4.08)

# Save to XYZ file
write('au_bulk.xyz', au_bulk)

# Read from XYZ file
read_au_bulk = read('au_bulk.xyz')

# Print atom types and positions
for atom in read_au_bulk:
    print(f'Atom type: {atom.symbol}, Position: {atom.position}')
