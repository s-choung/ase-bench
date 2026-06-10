from ase.db import connect
from ase.build import fcc111

# Connect to an ASE database or create if not exists
db = connect('cu_slabs.db')

# Generate Cu slab structures with 2, 3, and 4 layers and store in the database
for layers in [2, 3, 4]:
    atoms = fcc111('Cu', size=(3, 3, layers), vacuum=10.0)
    db.write(atoms, layers=layers)

# Retrieve and print the structure with layers=3
selection = db.select(layers=3)
for row in selection:
    print("Number of atoms in Cu slab with 3 layers:", len(row))
