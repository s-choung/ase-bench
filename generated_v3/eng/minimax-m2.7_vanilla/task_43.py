from ase.build import fcc100
from ase.db import connect

db = connect('cu_slabs.db')

for layers in [2, 3, 4]:
    slab = fcc100('Cu', size=(1, 1, layers))
    db.write(slab, layers=layers)

row = db.select(layers=3)[0]
print('Number of atoms in the 3‑layer slab:', len(row.toatoms()))
