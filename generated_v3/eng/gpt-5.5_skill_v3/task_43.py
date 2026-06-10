import os
from ase.build import fcc111
from ase.db import connect

dbfile = "cu_slabs.db"
if os.path.exists(dbfile):
    os.remove(dbfile)

db = connect(dbfile)

for layers in (2, 3, 4):
    slab = fcc111("Cu", size=(2, 2, layers), vacuum=10.0)
    db.write(slab, layers=layers)

for row in db.select(layers=3):
    atoms = row.toatoms()
    print(len(atoms))
