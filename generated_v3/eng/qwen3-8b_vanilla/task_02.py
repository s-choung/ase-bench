import numpy as np
from ase import Atoms
from ase.build import bulk, slab

bulk = bulk('Pt', 'fcc', a=3.92)
slab = slab(bulk, (1,1,1), 4, vacuum=10.0)
positions = slab.get_positions()
z_coords = positions[:,2]
top_index = np.argmax(z_coords)
top_pos = positions[top_index]
co = Atoms('CO', positions=[[0,0,0],[0,0,1.1]], cell=slab.get_cell())
co.translate(top_pos)
slab += co
print(len(slab))
