from ase.build import fcc100
slab = fcc100('Cu', size=(3, 3, 3), a=3.597, vacuum=12)
print(len(slab))
print(slab.cell)
