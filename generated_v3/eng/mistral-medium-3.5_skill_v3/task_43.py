from ase import Atoms
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.db import connect

with connect('cu_slabs.db') as db:
    for layers in [2, 3, 4]:
        slab = fcc111('Cu', size=(1, 1, layers), vacuum=10.0)
        slab.calc = EMT()
        db.write(slab, layers=layers)

with connect('cu_slabs.db') as db:
    for row in db.select(layers=3):
        print(len(row.toatoms()))
