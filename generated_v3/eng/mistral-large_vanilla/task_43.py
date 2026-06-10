from ase import Atoms
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.db import connect

db = connect('cu_slabs.db')

for layers in [2, 3, 4]:
    slab = fcc111('Cu', size=(2, 2, layers), vacuum=10)
    slab.calc = EMT()
    db.write(slab, layers=layers)

slab_3 = db.select(layers=3)[0]
print(slab_3.natoms)
