import os
from ase.build import fcc111
from ase.db import connect

db_file = 'cu_slabs.db'
if os.path.exists(db_file):
    os.remove(db_file)

db = connect(db_file)

# Create and save slabs with 2, 3, and 4 layers
for n_layers in [2, 3, 4]:
    slab = fcc111('Cu', size=(2, 2, n_layers), vacuum=10.0)
    db.write(slab, key_value_pairs={'layers': n_layers})

# Select the slab with 3 layers and get its Atoms object
row = next(db.select(layers=3))
atoms3 = row.toatoms()

# Print the number of atoms
print(f"Number of atoms in the 3-layer slab: {len(atoms3)}")
