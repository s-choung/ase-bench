from ase.build import surface
from ase.lattice.facecenteredcubic import Fcc

cu_surf = surface(Fcc('Cu', 3.615), (1,0,0), 3, 12).repeat((3,3,1))
print(len(cu_surf))
print(cu_surf.cell)
