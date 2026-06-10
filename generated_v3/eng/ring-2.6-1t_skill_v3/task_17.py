from ase.build import bulk, surface, add_vacuum

cu = bulk('Cu', 'fcc', a=3.6)
slab = surface(cu, (2, 1, 1), 3)
add_vacuum(slab, 10.0)

print(f'Number of atoms: {len(slab)}')
print(f'Cell:\n{slab.get_cell()}')
