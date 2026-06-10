from ase.build import fcc111
from ase.db import connect
from ase.calculators.emt import EMT

db = connect('cu_slab.db')
for layers in range(2, 5):
    slab = fcc111('Cu', size=(2, 2, layers), vacuum=10.0)
    slab.calc = EMT()
    db.write(slab, layers=layers)

for row in db.select(layers=3):
    atoms = row.toatoms()
    print(len(atoms))
