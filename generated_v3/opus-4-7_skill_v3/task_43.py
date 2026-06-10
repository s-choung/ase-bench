from ase.build import fcc111
from ase.db import connect
import os

dbfile = 'cu_slabs.db'
if os.path.exists(dbfile):
    os.remove(dbfile)

db = connect(dbfile)
for n in [2, 3, 4]:
    slab = fcc111('Cu', size=(2, 2, n), vacuum=10.0)
    db.write(slab, layers=n)

for row in db.select(layers=3):
    atoms = row.toatoms()
    print(f"layers=3, natoms={len(atoms)}")
