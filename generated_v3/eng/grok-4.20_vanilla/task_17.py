from ase.build import surface
from ase.lattice.cubic import FaceCenteredCubic

atoms = surface(FaceCenteredCubic('Cu'), (2, 1, 1), layers=3, vacuum=10.0)
print(len(atoms))
print(atoms.cell)
