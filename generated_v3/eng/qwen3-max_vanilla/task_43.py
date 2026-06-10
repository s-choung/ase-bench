from ase import Atoms
from ase.build import fcc111
from ase.db import connect

# Create and connect to database
db = connect('cu_slabs.db')

# Store slabs with different layer counts
for layers in [2, 3, 4]:
    slab = fcc111('Cu', size=(2, 2, layers), vacuum=10.0)
    db.write(slab, layers=layers)

# Retrieve slab with layers=3 and print atom count
for row in db.select(layers=3):
    print(len(row.toatoms()))
