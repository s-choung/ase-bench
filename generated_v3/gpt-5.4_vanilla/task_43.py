from ase.build import fcc111
from ase.db import connect

db = connect('cu_slabs.db')

for layers in [2, 3, 4]:
    atoms = fcc111('Cu', size=(2, 2, layers), vacuum=8.0)
    db.write(atoms, layers=layers)

for row in db.select(layers=3):
    atoms = row.toatoms()
    print(len(atoms))
