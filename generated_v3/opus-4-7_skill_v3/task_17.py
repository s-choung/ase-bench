from ase.build import bulk, surface

cu = bulk('Cu', 'fcc', a=3.6)
slab = surface(cu, (2, 1, 1), 3, vacuum=10.0)

print("Number of atoms:", len(slab))
print("Cell:")
print(slab.get_cell())
