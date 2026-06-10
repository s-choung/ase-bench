from ase.build import fcc110, add_vacuum
from ase import Atoms

slab = fcc110('Fe', size=(2, 2, 4), vacuum=10.0)
print(f"Number of atoms: {len(slab)}")
print(f"Cell size: {slab.get_cell()}")
