from ase.build import surface
from ase.calculators.emt import EMT

slab = surface('Cu', (1, 0, 0), layers=3, vacuum=12.0)
slab = slab.repeat((3, 3, 1))

slab.calc = EMT()

print("Number of atoms:", len(slab))
print("Cell:")
print(slab.cell)
