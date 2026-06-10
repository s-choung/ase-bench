from ase.build import surface, bulk

Fe_bulk = bulk('Fe', 'bcc', a=2.866)
slab = surface(Fe_bulk, (1, 1, 0), layers=4, size=(2, 2), vacuum=10)
print(len(slab))
print(slab.get_cell())
