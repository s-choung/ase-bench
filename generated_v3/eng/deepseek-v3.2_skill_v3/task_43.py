from ase.build import fcc111
from ase.db import connect

with connect('slabs.db') as db:
    for layers in [2, 3, 4]:
        slab = fcc111('Cu', size=(1, 1, layers), vacuum=8.0)
        db.write(slab, layers=layers)

with connect('slabs.db') as db:
    for row in db.select(layers=3):
        atoms = row.toatoms()
        print(f"Atoms with layers=3: {len(atoms)} atoms")
        break
