from ase.build import fcc111
from ase.db import connect

db = connect('cu_slabs.db')

for n in [2, 3, 4]:
    atoms = fcc111('Cu', size=(2, 2, n), orthogonal=True)
    db.write(atoms, layers=n)

row = next(db.select(layers=3))
print(len(row.toatoms()))
