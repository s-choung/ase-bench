from ase.build import fcc111
from ase.db import connect

# Create Cu slabs with 2, 3, 4 layers
slabs = [fcc111('Cu', size=(2, 2, l), vacuum=10.0) for l in range(2, 5)]

# Store in ASE database with layers count
db = connect('cu_slabs.db')
for slab, layers in zip(slabs, [2, 3, 4]):
    db.write(slab, key='layers', value=layers)

# Retrieve structure with layers=3
selected = db.select('layers=3')[0]
print(selected.get_number_of_atoms())
