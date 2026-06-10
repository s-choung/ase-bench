from ase.build import surface, add_vacuum
from ase import bulk

bulk = bulk('Cu', 'fcc', a=3.6)
slab = surface(bulk.get_cell(), (2,1,1), 3)
add_vacuum(slab, 10.0)
print(len(slab))
print(slab.get_cell())
