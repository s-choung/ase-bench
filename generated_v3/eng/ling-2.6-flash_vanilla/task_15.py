from ase.build import fcc100, cut
from ase import Atoms

surf = cut(fcc100("Cu", a=3.6, size=(3, 3, 3), vacuum=12), top=0)
print("Number of atoms:", len(surf))
print("Cell info:\n", surf.get_cell())
