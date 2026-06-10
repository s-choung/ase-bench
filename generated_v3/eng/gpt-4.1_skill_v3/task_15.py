from ase.build import fcc100
from ase.io import write
# Create Cu(100) surface: 3x3x3, 12 Å vacuum
slab = fcc100('Cu', size=(3,3,3), vacuum=12.0)
print(len(slab))
print(slab.get_cell())
