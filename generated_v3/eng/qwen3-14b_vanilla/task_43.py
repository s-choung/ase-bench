from ase import Database
from ase.build import bulk, Slab

cu = bulk('Cu', 'fcc', a=3.6)
db = Database('copper_slabs.db', 'w')
for layers in [2, 3, 4]:
    slab = Slab(cu, (1,0,0), (1,1), layers=layers)
    db.write(slab, layers=layers)
db = Database('copper_slabs.db', 'r')
entry = db.select(layers=3).first()
print(len(entry))
