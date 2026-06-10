from ase.build import fcc111
from ase.db import connect

# Initialize database and store slabs for 2/3/4 layers
db = connect('cu_slabs.db')
for n_layers in [2, 3, 4]:
    slab = fcc111('Cu', size=(2, 2, n_layers), vacuum=10.0)
    db.write(slab, layers=n_layers)

# Retrieve and print atom count for 3-layer slab
for row in db.select(layers=3):
    three_layer_slab = row.toatoms()
    print(f"Number of atoms in 3-layer Cu slab: {len(three_layer_slab)}")
