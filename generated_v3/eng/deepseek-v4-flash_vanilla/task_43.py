from ase.build import fcc111
from ase.db import connect

db = connect('cu_slabs.db')

for layers in [2, 3, 4]:
    slab = fcc111('Cu', size=(1, 1, layers), a=3.615, vacuum=10.0)
    db.write(slab, layers=layers)

row = db.get(layers=3)
atoms = row.toatoms()
print(len(atoms))
