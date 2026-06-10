from ase.build import bcc110

slab = bcc110('Fe', size=(2, 2, 4), vacuum=10.0)

print('Number of atoms:', len(slab))
print('Cell size:')
print(slab.cell)
