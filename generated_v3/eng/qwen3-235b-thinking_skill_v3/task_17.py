from ase.build import bulk, surface, add_vacuum

cu = bulk('Cu', 'fcc', cubic=True)
slab = surface(cu, indices=(2, 1, 1), layers=3, vacuum=0)
add_vacuum(slab, 10.0)
print(len(slab))
print(slab.cell)
