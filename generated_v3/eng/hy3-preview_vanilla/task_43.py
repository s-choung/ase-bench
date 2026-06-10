from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.db import connect

# Create and store Cu slabs with different layer counts
db = connect('cu_slabs.db', append=False)
for layers in [2, 3, 4]:
    slab = fcc111('Cu', size=(1,1,layers), vacuum=10.0, a=3.6)
    slab.calc = EMT()
    db.write(slab, layers=layers)

# Retrieve and print structure with 3 layers
for row in db.select(layers=3):
    atoms = row.toatoms()
    print(f"Number of atoms in 3-layer slab: {len(atoms)}")
