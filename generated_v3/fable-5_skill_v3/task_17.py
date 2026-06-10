from ase.build import bulk, surface, add_vacuum

cu = bulk('Cu', 'fcc', a=3.6)
slab = surface(cu, (2, 1, 1), layers=3)
add_vacuum(slab, 10.0)
slab.center(axis=2)

print("Number of atoms:", len(slab))
print("Cell:")
print(slab.cell)
