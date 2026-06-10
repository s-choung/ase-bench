from ase.lattice.cubic import FaceCenteredCubic
from ase import Atoms

cu = FaceCenteredCubic(directions=[[1,0,0],[0,1,0],[0,0,1]],
                         symbol='Cu',
                         size=(2,2,2),
                         pbc=True)
print(cu.cell)
print(len(cu))
