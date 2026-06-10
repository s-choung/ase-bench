from ase.build import bulk, surface, add_vacuum

cu_bulk = bulk('Cu', 'fcc', a=3.6, cubic=True)
slab = surface(cu_bulk, (2, 1, 1), layers=3)
add_vacuum(slab, 10.0)
print(len(slab))
print(slab.get_cell())
