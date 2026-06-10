from ase.build import fcc111
from ase.db import connect

db = connect('cu_slabs.db')

for n in [2, 3, 4]:
    atoms = fcc111('Cu', size=(2, 2, n), vacuum=10.0)
    db.write(atoms, layers=n)

for row in db.select(layers=3):
    atoms = row.toatoms()
    print(len(atoms))
