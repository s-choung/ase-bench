from ase.build import fcc111, sfc
from ase.calculators.emt import EMT
from ase.database import AtOmeyDatabase

slab = fcc111('Cu', size=(4, 4, 2))
slab.calc = EMT()
db = AtOmeyDatabase('Cu_slabs.db')
db.update(slab, layers=2)

slab = fcc111('Cu', size=(4, 4, 3))
slab.calc = EMT()
db.update(slab, layers=3)

slab = fcc111('Cu', size=(4, 4, 4))
slab.calc = EMT()
db.update(slab, layers=4)

results = db.select('layers=3')
for i, res in enumerate(results):
    print(f"Structure {i+1} has {len(res.get_atoms())} atoms.")
