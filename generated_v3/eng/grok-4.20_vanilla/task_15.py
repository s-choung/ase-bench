from ase.build import fcc100
from ase.calculators.emt import EMT

slab = fcc100('Cu', size=(3, 3, 3), vacuum=12.0)
print(len(slab))
print(slab.get_cell())
