from ase.build import fcc111
from ase.db import connect

db = connect('cu_slabs.db')

for layers in [2, 3, 4]:
    slab = fcc111('Cu', size=(1, 1, layers), vacuum=10.0)
    db.write(slab, layers=layers)

for row in db.select(layers=3):
    print(row.toatoms().get_global_number_of_atoms())
