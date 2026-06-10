from ase.build import fcc111
from ase.db import connect

# Create and store slabs with different layer counts
with connect('cu_slabs.db') as db:
    for layers in [2, 3, 4]:
        slab = fcc111('Cu', size=(2, 2, layers), vacuum=10.0)
        db.write(slab, layers=layers)

# Retrieve and print info for 3-layer slab
with connect('cu_slabs.db') as db:
    for row in db.select(layers=3):
        print(f'Number of atoms in 3-layer slab: {len(row.toatoms())}')
