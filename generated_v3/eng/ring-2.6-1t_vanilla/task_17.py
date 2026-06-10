from ase.build import surface
from ase.calculators.emt import EMT

slab = surface('Cu', (2, 1, 1), 3, vacuum=10.0)
slab.calc = EMT()

print('Number of atoms:', len(slab))
print('Cell:')
print(slab.cell)
