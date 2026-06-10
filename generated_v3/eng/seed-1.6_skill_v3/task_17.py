from ase.build import bulk, surface, add_vacuum

cu_bulk = bulk('Cu', 'fcc')
slab = surface(cu_bulk, (2,1,1), 3)
add_vacuum(slab, 10.0)
print(len(slab))
print(slab.get_cell())
