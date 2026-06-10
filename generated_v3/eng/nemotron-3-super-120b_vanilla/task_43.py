from ase.build import fcc111
from ase.db import connect

db = connect('cu_slabs.db')
for layers in [2, 3, 4]:
    slab = fcc111('Cu', size=(1, 1, layers), vacuum=10.0)
    db.write(slab, key_value=dict(layers=layers))

atoms = next(db.select(layers=3)).toatoms()
print(len(atoms))
