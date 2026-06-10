from ase.db import connect
from ase.build import fcc111

db = connect('slabs.db', append=False)
for nl in [2, 3, 4]:
    slab = fcc111('Cu', size=(2, 2, nl), vacuum=10.0)
    db.write(slab, layers=nl)

for row in db.select(layers=3):
    print(row.natoms)
    break
