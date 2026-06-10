from ase.build import surface, bulk

cu = bulk('Cu', 'fcc')
slab = surface(cu, (2, 1, 1), 3)
slab.center(vacuum=10, axis=2)

print('Number of atoms:', len(slab))
print('Cell:\n', slab.cell)
