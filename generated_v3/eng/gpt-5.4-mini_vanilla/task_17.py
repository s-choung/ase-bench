from ase.build import bulk, surface

cu_bulk = bulk('Cu', 'fcc', a=3.615)
slab = surface(cu_bulk, (2, 1, 1), 3, vacuum=10.0)

print(len(slab))
print(slab.cell)
