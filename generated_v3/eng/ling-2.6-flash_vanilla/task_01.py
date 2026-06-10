from ase import Atoms
from ase.lattice.cubic import FaceCenteredCubic

cu = FaceCenteredCubic('Cu', size=(1, 1, 1), latticeconstant=3.615)
supercell = cu * (2, 2, 2)

print(supercell.get_cell())
print(len(supercell))
