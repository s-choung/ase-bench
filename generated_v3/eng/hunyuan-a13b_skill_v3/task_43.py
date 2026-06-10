from ase.db import connect
from ase.build import fcc111

# Create or connect to the database
db = connect('cu_slabs.db')

# Generate and store Cu slab structures with different layer counts
layer_counts = [2, 3, 4]
for layers in layer_counts:
    slab = fcc111('Cu', size=(2, 2, layers), vacuum=10.0)
    db.write(slab, layers=layers)  # Store layers as a custom property

# Retrieve and print the structure with layers=3
slab_3 = db.select(layers=3)[0]
print(f"Number of atoms in layers=3 structure: {len(slab_3)}")

# Close the database connection
db.close()
