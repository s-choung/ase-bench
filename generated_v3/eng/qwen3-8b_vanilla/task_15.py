from ase.build import slab
from ase import Atoms

bulk = bulk('Cu', 'fcc', a=3.615)
slab = slab(bulk, (1,0,0), nlayers=3, size=(3,3,3), vacuum=12)
print(f"Number of atoms: {len(slab)}")
print("Cell:", slab.get_cell())
