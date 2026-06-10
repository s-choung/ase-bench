from ase.build import fcc111
from ase.db import connect

db = connect('slab.db')

for layers in [2, 3, 4]:
    slab = fcc111('Cu', size=(3, 3, layers), vacuum=10.0)
    db.write(slab, layers=layers)

rows = db.select('layers=3')
for row in rows:
    atoms = row.toatoms()
    print(f"layers=3: {len(atoms)} atoms")
