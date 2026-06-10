from ase.build import nanotube
from ase.cell import FaceCenteredCubic
import numpy as np

cnts = 6, 6
length = 4.0
atoms = nanotube(6, 6, length=length)          # CNNTube('CNT',6,6, length=4) or nanotube(6, 6, length=4)

print('Number of atoms:', len(atoms))
print('Cell: a=', atoms.get_cell()[0][0],
      'b=', atoms.get_cell()[1][1],
      'c=', atoms.get_cell()[2][2],
      'alpha=', atoms.get_cell_angles()[0],
      'beta=', atoms.get_cell_angles()[1],
      'gamma=', atoms.get_cell_angles()[2])
