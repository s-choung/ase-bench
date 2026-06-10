from ase.build import surface, bulk

slab = surface(bulk('Cu', 'fcc'), indices=(2, 1, 1), layers=3, vacuum=10.0)
print(len(slab))
print(slab.get_cell())
