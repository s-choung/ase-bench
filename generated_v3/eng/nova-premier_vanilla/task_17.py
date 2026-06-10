from ase.build import surface
from ase.lattice.cubic import FaceCenteredCubic

bulk = FaceCenteredCubic('Cu', size=(2, 2, 2))
surf = surface(bulk, (2, 1, 1), layers=3, vacuum=10)
print("Atoms:", len(surf))
print("Cell:\n", surf.cell)
