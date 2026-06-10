from ase import Atoms
from ase.build import fcc111
from ase.db import connect

# Connect to the database (creates a new file if it doesn't exist)
db = connect('cu_slabs.db')

# Create Cu slabs with 2, 3, and 4 layers and store them in the database
for layers in range(2, 5):
    slab = fcc111('Cu', size=(3, 3, layers), vacuum=10.0)
    slab.calc = None  # Ensuring the calculator is not set (optional for db write)
    slab.info['layers'] = layers  # Store the number of layers as metadata
    db.write(slab, step=0, layer=layers, comment=f'Copper slab with {layers} layers')

# Retrieve the slab with exactly 3 layers
query = {'layer': 3}
for row in db.select(query):
    slab = row.toatoms()
    print(f'Number of atoms for 3-layer Cu slab: {slab.natoms}')

db.close()
