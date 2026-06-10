from ase.build import fcc111
from ase.db import connect
from ase.calculators.emt import EMT

db = connect('cu_slabs.db', append=False)

for n in (2, 3, 4):
    slab = fcc111('Cu', size=(3, 3, n), vacuum=10.0)
    slab.calc = EMT()
    slab.get_potential_energy()
    db.write(slab, layers=n)

for row in db.select(layers=3):
    print('layers=3, natoms =', row.natoms)
