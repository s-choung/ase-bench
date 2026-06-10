from ase.build import fcc111
from ase.db import connect
from ase.calculators.emt import EMT

db = connect('cu_slabs.db')

for layers in [2, 3, 4]:
    slab = fcc111('Cu', size=(2, 2, layers), vacuum=10.0)
    slab.set_calculator(EMT())
    db.write(slab, layers=layers)

result = db.select(layers=3)
for row in result:
    print(len(row.atoms))
