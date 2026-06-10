from ase.build import bulk, surface
from ase.calculators.emt import EMT

bulk = bulk('Cu', 'fcc', a=3.6)
surf = surface(bulk, (2,1,1), size=(1,1,3), vacuum=10.0)
print(len(surf))
print(surf.get_cell())
