from ase.build import surface
from ase.lattice.cubic import FaceCenteredCubic

# Create Cu bulk
cu = FaceCenteredCubic('Cu', latticeconstant=3.6)

# Cut (2,1,1) surface with 3 layers and 10 Å vacuum
surf = surface(cu, (2, 1, 1), 3, vacuum=10.0)

# Print number of atoms and cell
print(len(surf))
print(surf.cell)
