from ase.build import fcc111
from ase.db import connect

# Create Cu(111) slabs with 2, 3, 4 layers
surfaces = []
for nlayers in [2, 3, 4]:
    slab = fcc111('Cu', size=(2, 2, nlayers), vacuum=10.0)
    surfaces.append((slab, nlayers))

# Store in ASE database
with connect('cu_slabs.db') as db:
    for slab, nlayers in surfaces:
        db.write(slab, layers=nlayers)

# Retrieve structure with layers=3
with connect('cu_slabs.db') as db:
    row = db.select(layers=3)[0]
    print(row.natoms)
