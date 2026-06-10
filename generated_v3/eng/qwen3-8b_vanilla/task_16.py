import ase
from ase.build import slab

bulk = ase.build.bulk('Fe', 'bcc', a=2.86)
slab = slab(bulk, (1,1,0), size=(2,2,4), vacuum=10)

print(f"Number of atoms: {len(slab)}")
print(f"Cell size (angstroms): {slab.get_cell()}")
