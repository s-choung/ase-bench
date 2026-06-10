from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.db import connect

db = connect('cu_slabs.db')

for n in [2, 3, 4]:
    slab = fcc111('Cu', size=(2, 2, n), vacuum=10.0)
    slab.calc = EMT()
    db.write(slab, layers=n)

selection = db.select(layers=3)
for row in selection:
    print(len(row.atoms))
