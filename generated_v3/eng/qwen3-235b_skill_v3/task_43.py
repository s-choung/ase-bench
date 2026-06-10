from ase import db
from ase.build import fcc111
from ase import Atoms

# Create a database
d = db.connect('cu_slabs.db')

# Generate Cu(111) slabs with 2, 3, 4 layers and store in database
for layers in [2, 3, 4]:
    slab = fcc111('Cu', size=(2, 2, layers), vacuum=10.0)
    d.write(slab, layers=layers)

# Retrieve the structure with layers=3
row = d.select(layers=3)[0]
print(len(row.toatoms()))
