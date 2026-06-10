from ase.db import connect
from ase.build import fcc111

db = connect('cu_slabs.db')

for n in [2, 3, 4]:
    slab = fcc111('Cu', n, vacuum=10)
    db.write(slab, layers=n)

row = db.select(layers=3).fetchone()
print(len(row.toatoms()))
