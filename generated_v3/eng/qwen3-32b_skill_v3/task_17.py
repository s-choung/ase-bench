from ase.build import bulk, surface, add_vacuum

cu_bulk = bulk('Cu', 'fcc')
slab = surface(cu_bulk, (2, 1, 1), layers=3)
add_vacuum(slab, 10.0)
print(len(slab), slab.get_cell())
