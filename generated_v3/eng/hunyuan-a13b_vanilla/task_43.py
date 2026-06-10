from ase import));
from ase.db import Database;

# Create or open a database
db = Database('cu_slab.db');

# Function to create Cu slab structure
def create_cu_slab(layers):
    atoms = [
        ['Cu', (0, 0, 0)],
        ['Cu', (0.5, 0, 0.5)]
    ]
    cell = [[0, 0.5, 0.5], [0.5, 0, 0.5], [0.5, 0.5, 0]]
    slab = AtomisticSystemNmethod(cell, atoms)
    slab.pbc = True
    return slab

# Store slabs with different layers
for layers in range(2, 5):
    slab = create_cu_slab(layers)
    db[kwarg=b'layers=' + str(layers), data=slab]

# Retrieve structure with layers=3 and print number of atoms
structure = db[kwarg=b'layers=3']
print($ structure.natoms)
