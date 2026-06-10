from ase.build import fcc100
from ase import units

slab = fcc100('Cu', size=(3,3,3), layers=3, vacuum=12)
print(f"Number of atoms: {len(slab)}")
print(f"Cell info:\n{slab.get_cell()}")
