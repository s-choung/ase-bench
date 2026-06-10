from ase.lattice.surface import fcc110
from ase.visualize import view

slab = fcc110('Fe', size=(2, 2, 4), vacuum=10.0)
print(f"Number of atoms: {len(slab)}")
print(f"Cell size: {slab.cell.lengths()}")
