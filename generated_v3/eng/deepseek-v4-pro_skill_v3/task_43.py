from ase.build import fcc111
from ase.db import connect

# Create a fresh database
db = connect('cu_slabs.db', append=False)

# Build Cu(111) slabs with 2, 3 and 4 layers, store with key 'layers'
a = 3.61        # Cu lattice constant
vacuum = 10.0   # vacuum gap
size = (2, 2, None)  # xy size

for n in [2, 3, 4]:
    atoms = fcc111('Cu', size=(size[0], size[1], n), a=a, vacuum=vacuum)
    db.write(atoms, layers=n)

# Retrieve only the 3‑layer slab and print its number of atoms
for row in db.select(layers=3):
    print(len(row.toatoms()))
