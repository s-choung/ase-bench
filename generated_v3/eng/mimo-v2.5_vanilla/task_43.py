from ase.build import surface
from ase.db import connect

db = connect('cu_slabs.db')

for n in [2, 3, 4]:
    slab = surface('Cu', (1, 1, 1), layers=n, vacuum=10.0)
    db.insert(slab, layers=n)

for row in db.select(layers=3):
    atoms = row.toatoms()
    print(len(atoms))
