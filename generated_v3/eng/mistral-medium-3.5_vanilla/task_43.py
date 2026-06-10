from ase.build import fcc111
from ase.db import connect
from ase.io import write

with connect('cu_slabs.db') as db:
    for layers in [2, 3, 4]:
        slab = fcc111('Cu', (1, 1, layers), vacuum=5)
        db.write(slab, layers=layers)

with connect('cu_slabs.db') as db:
    for row in db.select(layers=3):
        print(len(row.toatoms()))
