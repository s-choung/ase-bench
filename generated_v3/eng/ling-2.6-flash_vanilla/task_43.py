from ase import Atoms
from ase.db import connect

# Create and store Cu slabs with different layer counts
with connect('cu_slabs.db') as db:
    for layers in [2, 3, 4]:
        slab = fcc111('Cu', size=(3, 3, layers), vacuum=10.0)
        slab.calc = EMT()  # Use built-in EMT calculator
        db.write(slab, layers=layers)

# Retrieve and print number of atoms for the 3-layer slab
with connect('cu_slabs.db') as db:
    result = db.select(layers=3)
    for row in result:
        print(row.toatoms().get_number_of_atoms())
