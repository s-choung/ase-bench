from ase.build import surface
slab = surface('Fe', 'bcc110', size=(2, 2, 4), vacuum=10)
print(len(slab))
print(slab.cell)
