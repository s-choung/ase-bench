from ase.build import fcc111
from ase.db import connect
from ase.calculators.emt import EMT

db = connect('cu_slabs.db', append=False)

for n in [2, 3, 4]:
    slab = fcc111('Cu', size=(1, 1, n), vacuum=5.0)
    slab.calc = EMT()
    db.write(slab, layers=n)

for row in db.select(layers=3):
    print(row.natoms)
