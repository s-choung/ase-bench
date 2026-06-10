from ase import bulk
from ase.build import surface, add_vacuum

cu_bulk = bulk('Cu', 'fcc', a=3.6)
cu_surface = surface(cu_bulk, (2, 1, 1), 3)
add_vacuum(cu_surface, 10.0)

print("Number of atoms:", len(cu_surface))
print("Cell:\n", cu_surface.get_cell())
