from ase.build import bulk, surface, add_vacuum

slab = surface(bulk('Cu', 'fcc', a=3.6, cubic=True), (2, 1, 1), 3)
add_vacuum(slab, 10.0)

print('Number of atoms:', len(slab))
print('Cell:\n', slab.get_cell())
