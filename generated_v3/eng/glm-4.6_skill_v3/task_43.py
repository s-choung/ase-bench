from ase.build import fcc111
from ase.db import connect

db = connect('cu_slabs.db')

for layers in [2, 3, 4]:
    slab = fcc111('Cu', size=(2, 2, layers), vacuum=10.0)
    db.write(slab, layers=layers)

atoms = db.select(layers=3)[0].toatoms()
print(atoms.get_number_of_atoms())
