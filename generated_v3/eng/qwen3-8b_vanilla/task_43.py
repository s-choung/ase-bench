import ase.db
from ase.build import slabs
from ase.calculators.emt import EMT

db = ase.db.connect('slabs.db')

for l in [2, 3, 4]:
    slab = slabs('Cu', '100', layers=l, size=(1, 1, 1), vacuum=5.0)
    slab.set_calculator(EMT())
    db.write(slab, layers=l)

sel = db.select(layers=3)
print(len(sel[0]))
