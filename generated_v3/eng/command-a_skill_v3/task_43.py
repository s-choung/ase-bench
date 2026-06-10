from ase.build import fcc111
from ase.db import connect

db = connect('cu_slabs.db', 'w', if_exists='overwrite')

for layers in [2, 3, 4]:
    slab = fcc111('Cu', size=(2, 2, layers), vacuum=10.0)
    db.write(slab, layers=layers)

with connect('cu_slabs.db') as db:
    atoms = db.get(layers=3).toatoms()
    print(len(atoms))
