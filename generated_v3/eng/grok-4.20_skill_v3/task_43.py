from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.db import connect
from ase.optimize import BFGS

db = connect('cu_slabs.db', append=False)

for layers in [2, 3, 4]:
    slab = fcc111('Cu', size=(3, 3, layers), vacuum=10.0)
    slab.calc = EMT()
    BFGS(slab).run(fmax=0.05)
    db.write(slab, layers=layers)

row = list(db.select(layers=3))[0]
print(row.natoms)
