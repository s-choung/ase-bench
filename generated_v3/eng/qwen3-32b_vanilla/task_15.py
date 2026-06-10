from ase.build import fcc100

slab = fcc100('Cu', (3, 3), layers=3, vacuum=12)
print(len(slab))
print(slab.cell)
