from ase.db import connect
from ase.build import fcc111

db = connect('cu_slabs.db')

for n_layers in [2, 3, 4]:
    slab = fcc111('Cu', size=(2, 2), a=3.61, layers=n_layers)
    db.write(slab, layers=n_layers)

for row in db.select(layers=3):
    print(f"Number of atoms: {len(row.toatoms())}")
