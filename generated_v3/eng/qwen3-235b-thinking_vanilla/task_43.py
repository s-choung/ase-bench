from ase.build import fcc111
from ase.db import connect

db = connect('slabs.db', append=False)
for layers in [2, 3, 4]:
    slab = fcc111('Cu', (1, 1, layers), vacuum=10.0)
    db.write(slab, layers=layers)
row = next(db.select(layers=3))
print(row.natoms)
