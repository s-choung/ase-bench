from ase.build import bulk, surface
from ase.calculators.emt import EMT

cu_bulk = bulk('Cu', 'fcc', a=3.615)
slab = surface(cu_bulk, (2, 1, 1), 3, vacuum=10.0)
slab.calc = EMT()

print('Number of atoms:', len(slab))
print('Cell:')
print(slab.cell)
