from ase.build import fcc111
from ase.db import connect
db = connect('cu.db', append=False)
for n in [2, 3, 4]:
    atoms = fcc111('Cu', (1, 1, n), vacuum=10.0)
    db.write(atoms, layers=n)
for row in db.select(layers=3):
    print(len(row.toatoms()))
