from ase.build import fcc111
from ase.db import connect

# Initialize database
db = connect('cu_slabs.db')
db.purge()  # Clear previous data for clean run

# Store Cu slab structures for 2, 3, and 4 layers
for layers in [2, 3, 4]:
    slab = fcc111('Cu', size=(3, 3, layers), vacuum=10.0)
    db.write(slab, layers=layers)

# Retrieve only the structure with layers=3 using select()
target_slab = db.select(layers=3)

# Print the number of atoms of the retrieved structure
if target_slab:
    # select() returns an iterator/generator; get the first result
    atoms = next(iter(target_slab))
    print(f"Atoms in 3-layer slab: {len(atoms)}")
