from ase.build import surface
from ase.db import connect

db = connect('cu_slabs.db')
for n in (2, 3, 4):
    db.write(surface('Cu', (1, 1, 1), n, vacuum=10.0, size=(2, 2, 1)), layers=n)

print(next(db.select('layers=3')).natoms)
