from ase.build import fcc111
from ase.io import connect
from ase.calculators.emt import EMT

# Create slabs with different layer counts
slabs = {}
for layers in [2, 3, 4]:
    slab = fcc111('Cu', size=(2, 2, layers), vacuum=10.0)
    slab.calc = EMT()
    slabs[f'layers={layers}'] = slab

# Connect to the database
db = connect('cu_slabs.db')

# Write the slabs to the database
for key, slab in slabs.items():
    db.write(slab, key=key)

# Close the database connection
db.close()

# Reconnect to the database
db = connect('cu_slabs.db')

# Select the slab with layers=3
slab_3_layers = db.select(key='layers=3')[0]

# Print the number of atoms in the selected slab
print(f"Number of atoms in slab with layers=3: {len(slab_3_layers)}")

# Close the database connection
db.close()
