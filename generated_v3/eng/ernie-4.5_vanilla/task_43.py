from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.db import connect

# Create a database
db = connect('cu_slabs.db')

# Create Cu slabs with different layer counts
for layers in [2, 3, 4]:
    slab = fcc111('Cu', size=(1, 1, layers), vacuum=10.0)
    slab.set_calculator(EMT())  # Optional: if you want to compute energy or forces
    # Store structure and layer information in the database
    db.write(slab, layers=layers)

# Retrieve the structure with layers=3 and print its number of atoms
for row in db.select(layers=3):
    print(f"Number of atoms: {len(row.toatoms())}")
