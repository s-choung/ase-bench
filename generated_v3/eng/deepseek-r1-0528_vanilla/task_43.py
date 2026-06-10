from ase.build import fcc100
from ase.db import connect

db = connect('cu_slabs.db')
for n in [2, 3, 4]:
    slab = fcc100('Cu', size=(1, 1, n), vacuum=7.5)
    db.write(slab, layers=n)

row = next(db.select(layers=3))
atoms = row.toatoms()
print(len(atoms))
