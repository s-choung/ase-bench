from ase.build import fcc111
from ase.db import connect

db = connect('cslab.db')
for layers in [2, 3, 4]:
    slab = fcc111('Cu', size=(2, 2, layers), vacuum=10.0)
    db.write(slab, layers=layers)

results = db.select(layers=3)
for row in results:
    print(len(row.toatoms()))
