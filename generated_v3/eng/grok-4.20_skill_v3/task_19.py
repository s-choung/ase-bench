from ase import Atoms
from ase.geometry import get_distances
import numpy as np

atoms = Atoms('CO2',
              positions=[[0, 0, 0],
                         [0, 0, 1.16],
                         [0, 0, -1.16]],
              cell=[10, 10, 10],
              pbc=False)

d = get_distances(atoms.positions, cell=atoms.cell, pbc=atoms.pbc)
print(np.round(d[0], 4))
