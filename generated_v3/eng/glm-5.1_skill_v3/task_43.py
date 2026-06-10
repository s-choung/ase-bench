from ase.build import fcc111
from ase.db import connect

db = connect('cu_slabs.db')

for n in [2, 3, 4]:
    slab = fcc111('Cu', size=(1, 1, n), vacuum=10.0)
    db.write(slab, layers=n)

row = list(db.select(layers=3))[0]
print(row.natoms)
