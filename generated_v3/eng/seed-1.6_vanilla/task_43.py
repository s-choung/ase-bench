from ase.build import bulk, fcc111
from ase.db import connect

# Generate Cu bulk and store slabs in DB
cu_bulk = bulk('Cu')
with connect('cu_slabs.db') as db:
    for layers in [2, 3, 4]:
        slab = fcc111(cu_bulk, layers=layers, vacuum=10.0)
        db.write(slab, layers=layers)

# Retrieve 3-layer slab and print atom count
with connect('cu_slabs.db') as db:
    for row in db.select(layers=3):
        print(row.toatoms().get_number_of_atoms())
