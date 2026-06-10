from ase.build import fcc100
from ase.calculators.emt import EMT
from ase.db import connect

db = connect("cu_slabs.db")

for nlayers in [2, 3, 4]:
    slab = fcc100("Cu", size=(1, 1, nlayers), vacuum=5.0)
    slab.calc = EMT()
    db.write(slab, layers=nlayers)

# retrieve only the structure with layers=3
for row in db.select(layers=3):
    atoms = row.toatoms()
    print(len(atoms))
