from ase import Atoms
from ase.build import surface

slab = surface('Fe', (1,1,0), layers=4, vacuum=10)
slab = slab.repeat((2,2,1))
print(len(slab))
print(slab.cell)
