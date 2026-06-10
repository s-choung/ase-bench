from ase.build import fcc111
from ase.db import connect
from ase.calculators.emt import EMT

db = connect('cu_slabs.db')

for layers in [2, 3, 4]:
    slab = fcc111('Cu', size=(4, 4, layers), vacuum=10.0, periodic=True)
    slab.calc = EMT()
    slab.get_potential_energy()
    db.write(slab, layers=layers)

atoms = list(db.select(layers=3))[0].toatoms()
print(len(atoms))
