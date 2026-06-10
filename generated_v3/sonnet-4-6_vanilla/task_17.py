from ase.build import bulk, surface
from ase.visualize import view

cu_bulk = bulk('Cu', 'fcc', a=3.615)

slab = surface(cu_bulk, (2, 1, 1), layers=3, vacuum=10.0)

print(f"Number of atoms: {len(slab)}")
print(f"Cell:\n{slab.get_cell()}")
print(f"Cell lengths and angles: {slab.cell.cellpar()}")
