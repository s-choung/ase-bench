from ase.build import bulk, slab
from ase.ase.db import connect, write, select

# Create slabs with different layer counts
slab_2_layers = slab('Cu', layers=(1, 1), size=(3, 3, 3), vacuum=10.0, space='lattice')
slab_3_layers = slab('Cu', layers=(1, 1), size=(3, 3, 3), vacuum=10.0, space='lattice')
slab_4_layers = slab('Cu', layers=(1, 1, 1), size=(3, 3, 3), vacuum=10.0, space='lattice')

# Store the slabs in a database with layers count as key-value pair
db = connect('my_copper_slabs.db')
key_values = {
    'layers': 2,
    'layers_2': slab_2_layers.get_layers()[1],
    'layers_3': slab_3_layers.get_layers()[1],
    'layers_4': slab_4_layers.get_layers()[2],
}

db.write(slab_2_layers, key='layers_2')
db.write(slab_3_layers, key=key_values['layers_3'])
db.write(slab_4_layers, key=key_values['layers_4'])
