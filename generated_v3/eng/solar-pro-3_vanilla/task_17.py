from ase import Atoms
from ase.build import surface
from ase.visualize import view   # comment-out if GUI not desired

# bulk Cu (fcc)
cu = Atoms('Cu', positions=[[0,0,0]], cell=[(3.61,0,0),(0,3.61,0),(0,0,3.61)], pbc=True)

# carve (2,1,1) surface, keep 3 layers
N = 3                     # number of layers to keep
cu_surface = surface(cu, (2,1,1), nlayers=3)

# add vacuum in z‑direction (10 Å)
cu_surface.cell[2] += 10.0

# print basic information
print(f'Number of atoms: {len(cu_surface)}')
print('Cell parameters:')
print(cu_surface.cell)
