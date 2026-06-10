from ase.build import bulk, surface, add_vacuum
cu = bulk('Cu', 'fcc', a=3.615)
slab = surface(cu, (2,1,1), layers=3)
add_vacuum(slab, 10)
print(len(slab))
print(slab.get_cell())
