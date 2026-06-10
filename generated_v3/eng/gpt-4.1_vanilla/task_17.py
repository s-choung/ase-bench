from ase.build import bulk, surface
from ase.visualize import view

# Bulk Cu
atoms = bulk('Cu', 'fcc', a=3.615)
# Create (2,1,1) surface with 3 layers
slab = surface(atoms, (2,1,1), 3)
slab.center(vacuum=10, axis=2)

print('Number of atoms:', len(slab))
print('Cell:')
print(slab.cell)
