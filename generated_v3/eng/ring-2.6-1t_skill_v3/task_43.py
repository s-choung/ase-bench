from ase.build import fcc111
from ase.db import connect

db = connect('cu_slabs.db')

for nlayers in [2, 3, 4]:
    slab = fcc111('Cu', size=(2, 2, nlayers), vacuum=10.0)
    db.write(slab, layers=nlayers)

for row in db.select(layers=3):
    print(row.natoms)

db.close()
