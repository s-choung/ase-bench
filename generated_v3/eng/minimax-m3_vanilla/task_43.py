from ase import Atoms
from ase.build import fcc111
from ase.db import connect

db = connect('cu_slabs.db')

# Create Cu slabs with 2, 3, 4 layers and store in database
for n in [2, 3, 4]:
    slab = fcc111('Cu', size=(1, 1, n), vacuum=5.0)
    db.write(slab, layers=n, metal='Cu', surface='fcc111')

# Retrieve and inspect the 3-layer slab
db = connect('cu_slabs.db')
row = db.select(layers=3).next()
print(f"Number of atoms in 3-layer Cu slab: {row.natoms}")
