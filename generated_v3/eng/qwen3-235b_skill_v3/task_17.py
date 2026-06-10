from ase import Atoms
from ase.build import bulk, surface
from ase.io import write

# Create bulk Cu
cu_bulk = bulk('Cu', 'fcc', a=3.6)

# Cut (2,1,1) surface with 3 layers
slab = surface(cu_bulk, indices=(2,1,1), layers=3, vacuum=10.0)

# Print number of atoms and cell
print(len(slab))
print(slab.get_cell())
