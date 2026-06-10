from ase.build import fcc100

slab = fcc100('Cu', size=(3, 3, 3), vacuum=12.0, a=3.6)
print(len(slab))
print(slab.get_cell())
