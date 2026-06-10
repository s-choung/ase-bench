from ase.build import bulk, surface
cu_slab = surface(bulk('Cu', 'fcc', cubic=True), (2, 1, 1), layers=3, vacuum=10)
print(len(cu_slab))
print(cu_slab.cell)
