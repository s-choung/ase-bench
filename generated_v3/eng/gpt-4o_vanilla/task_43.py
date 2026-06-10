from ase.build import fcc111
from ase.db import connect
from ase.calculators.emt import EMT

db = connect('structures.db')

for layers in [2, 3, 4]:
    slab = fcc111('Cu', size=(2, 2, layers))
    slab.calc = EMT()
    slab.info['layers'] = layers
    db.write(slab)

slab_with_three_layers = db.select(layers=3).next()
print('Number of atoms:', len(slab_with_three_layers))
