from ase.build import fcc100
from ase.calculators.emt import EMT
from ase.db import connect

# Initialize ASE database
db = connect('cu_slabs.db')

# Create and store slabs for 2, 3, 4 layers
for nlayers in [2, 3, 4]:
    slab = fcc100('Cu', size=(3, 3, nlayers), vacuum=10.0)
    slab.calc = EMT()
    db.write(slab, layers=nlayers)

# Retrieve and print atom count for 3-layer slab
for row in db.select(layers=3):
    three_layer_slab = row.toatoms()
    print(len(three_layer_slab))
