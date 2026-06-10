from ase.build import bulk, surface, add_vacuum
from ase.lattice.cubic import SimpleCubic

cu = bulk('Cu', 'fcc', a=3.6)
slab = surface(cu, (2, 1, 1), layers=3)
add_vacuum(slab, vacuum=10.0)
print(len(slab), slab.cell)
