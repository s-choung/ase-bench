from ase.db import connect
from ase.build import surface

db = connect('cu_slabs.db')
for n in [2, 3, 4]:
    atoms = surface('Cu', (111), layers=n, vacuum=10.0)
    db.write(atoms, layers=n)

row = next(db.select(layers=3))
print(len(row.toatoms()))
