from ase.build import bulk, surface

atoms = bulk('Cu', cubic=True)
layer = atoms.repeat((3, 3, 1))
slab = surface(layer, (2, 1, 1), layers=3, periodic=True)
slab.center(vacuum=10, axis=2)

print(f'Number of atoms: {len(slab)}')
print('Cell:')
print(slab.get_cell())
