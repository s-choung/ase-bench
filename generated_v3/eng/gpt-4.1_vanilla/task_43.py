from ase.build import fcc111
from ase.db import connect

db = connect('cuslabs.db')

for n_layers in [2, 3, 4]:
    slab = fcc111('Cu', size=(2, 2, n_layers), vacuum=10.0)
    db.write(slab, layers=n_layers)

row = next(db.select(layers=3))
print(len(row.toatoms()))
