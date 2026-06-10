from ase.build import bulk, surface
from ase.calculators.emt import EMT

slab = surface(bulk('Cu'), (2, 1, 1), 3)
slab.center(vacuum=10.0, axis=2)
slab.calc = EMT()

print(len(slab))
print(slab.cell)
