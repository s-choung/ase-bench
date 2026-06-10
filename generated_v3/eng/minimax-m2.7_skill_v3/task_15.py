from ase.build import fcc100
from ase import Atoms

slab = fcc100('Cu', size=(3, 3, 3), vacuum=12)
print(f"Number of atoms: {len(slab)}")
print(f"Cell vectors:\n{slab.get_cell()}")
print(f"Cell lengths and angles: {slab.get_cell_lengths_and_angles()}")
