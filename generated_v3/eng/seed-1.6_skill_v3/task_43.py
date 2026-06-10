from ase.db import connect
from ase.build import fcc111

# Store slabs with 2,3,4 layers in database
with connect('cu_slabs.db') as db:
    for layers in [2, 3, 4]:
        slab = fcc111('Cu', size=(2, 2, layers), vacuum=10.0)
        db.write(slab, layers=layers)

# Retrieve and print atom count for 3-layer slab
for row in connect('cu_slabs.db').select(layers=3):
    print(len(row.toatoms()))
