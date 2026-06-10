from ase.build import fcc111
from ase.db import connect
db = connect('cu.db')
for n in [2, 3, 4]:
    slab = fcc111('Cu', (1, 1, n), vacuum=10)
    db.write(slab, layers=n)
for row in db.select(layers=3):
    print(row.natoms)
