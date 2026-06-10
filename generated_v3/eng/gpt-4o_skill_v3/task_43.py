from ase.build import fcc111
from ase.db import connect

slabs = [fcc111('Cu', size=(2, 2, layers), vacuum=10.0) for layers in [2, 3, 4]]

db = connect('cu_slabs.db')
for slab in slabs:
    db.write(slab, layers=len(slab) // 4)  # layers count

rows = db.select(layers=3)
for row in rows:
    print('Number of atoms in the slab with 3 layers:', row.natoms)
