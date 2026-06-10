from ase.build import fcc111
from ase.db import connect

# Create database and store slabs
db = connect('cu_slabs.db')
for layers in [2, 3, 4]:
    slab = fcc111('Cu', size=(2, 2, layers), vacuum=10.0)
    db.write(slab, layers=layers)

# Retrieve and print structure with layers=3
for row in db.select(layers=3):
    atoms = row.toatoms()
    print(f"Number of atoms in 3-layer slab: {len(atoms)}")
