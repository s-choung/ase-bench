from ase.db import connect
from ase.build import fcc111

# Create database and store slabs
db = connect('cu_slabs.db')
for layers in [2, 3, 4]:
    slab = fcc111('Cu', size=(1, 1, layers), vacuum=10.0)
    db.write(slab, layers=layers)

# Retrieve and print atom count for layers=3
atoms = db.select(layers=3)[0].toatoms()
print(len(atoms))
