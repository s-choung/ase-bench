from ase.db import connect
from ase import Atoms
from ase.io import TrajectoryWriter
from ase.build import surface
from ase.build import make_supercell

# Define Cu slabs with different layer counts
layer_counts = [2, 3, 4]
base_lattice = [(12, 12, 1), (12, 12, 12)]
vacuum = 15

# Create a new database file
db = connect('slabs.db')

for n_layers in layer_counts:
    # Build the slab structure
    slab = surface('Cu', (1, 1), n_layers, vacuum=vacuum, a=base_lattice[n_layers-2])
    # Store the structure with layer count as a key-value pair
    db.write(slab=slab, layers=n_layers)

# Retrieve and print the number of atoms for the structure with 3 layers
retrieved_slab = db.select(table='slab', where='layers == 3')
for slab in retrieved_slab:
    print(f'Number of atoms in slab with 3 layers: {len(slab)}')
