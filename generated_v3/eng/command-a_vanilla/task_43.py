from ase.db import connect
from ase.build import fcc111
from ase import Atoms

# Create Cu slab structures with different layer counts
slabs = {
    2: fcc111('Cu', size=(2, 2, 2), vacuum=10.0),
    3: fcc111('Cu', size=(2, 2, 3), vacuum=10.0),
    4: fcc111('Cu', size=(2, 2, 4), vacuum=10.0)
}

# Connect to ASE database
with connect('cu_slabs.db') as db:
    for layers, slab in slabs.items():
        db.write(slab, layers=layers)

# Retrieve structure with layers=3
with connect('cu_slabs.db') as db:
    row = db.select(layers=3)[0]
    atoms = row.toatoms()
    print(len(atoms))
