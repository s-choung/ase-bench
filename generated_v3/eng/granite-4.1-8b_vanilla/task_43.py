from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.io import write, read
from ase.db import connect

def create_cu_slab(layers):
    slab = fcc111('Cu', size=(3, 3, layers), vacuum=10.0)
    return slab

# Create Cu slabs with different layer counts
for layers in [2, 3, 4]:
    slab = create_cu_slab(layers)
    slab.info['layers'] = layers  # Store layer count as metadata
    db = connect('cu_slabs.db')
    db.write(slab)

# Retrieve the slab with 3 layers and print its number of atoms
db = connect('cu_slabs.db')
for entry in db.select(layers=3):
    print(entry.numatoms)
