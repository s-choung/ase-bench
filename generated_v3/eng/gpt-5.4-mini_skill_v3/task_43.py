from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.db import connect

db = connect('cu_slabs.db')

for layers in [2, 3, 4]:
    slab = fcc111('Cu', size=(2, 2, layers), vacuum=10.0)
    slab.calc = EMT()
    db.write(slab, layers=layers)

for row in db.select(layers=3):
    atoms = row.toatoms()
    print(len(atoms))
    break
