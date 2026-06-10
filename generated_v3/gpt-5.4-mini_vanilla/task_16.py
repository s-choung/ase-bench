from ase.build import surface
from ase.calculators.emt import EMT

slab = surface('Fe', (1, 1, 0), layers=4, vacuum=10.0, periodic=True)
slab = slab.repeat((2, 2, 1))
slab.calc = EMT()

print("Number of atoms:", len(slab))
print("Cell:\n", slab.cell)
