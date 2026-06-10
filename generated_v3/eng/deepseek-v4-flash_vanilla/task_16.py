from ase.build import bulk, surface
from ase.io import write

# Create Fe BCC(110) surface
fe_bulk = bulk('Fe', 'bcc', a=2.8665)
slab = surface(fe_bulk, (1,1,0), layers=4, size=(2,2,4), vacuum=10)

# Print number of atoms and cell size
print(len(slab))
print(slab.cell)
