from ase import Atoms
from ase.calculators.emt import EMT
from ase.db import connect
from ase.build import fcc111

db = connect('cu_slabs.db')

for layers in range(2, 5):
    slab = fcc111('Cu', size=(2,2,layers), vacuum=10.0)
    slab.calc = EMT()
    slab.get_potential_energy()
    db.write(slab, layers=layers)

for row in db.select(layers=3):
    print(row.natoms)
