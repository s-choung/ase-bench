from ase import Atoms
from ase.build import surface

slab = surface("Cu", (2, 1, 1), 3, vacuum=10)
print(f"Atoms: {len(slab)}, Cell: {slab.get_cell().tolist()}")
