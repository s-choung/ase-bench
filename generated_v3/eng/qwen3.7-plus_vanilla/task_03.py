from ase import Atoms
import numpy as np

a = 3.16
atoms = Atoms('MoS2',
              positions=[(0, 0, 0),
                         (a/2, -a/(2*np.sqrt(3)), 1.57),
                         (a/2, a/(2*np.sqrt(3)), -1.57)],
              cell=[a, a, 20.0, 90, 90, 120],
              pbc=[True, True, True])

atoms.center(vacuum=10.0, axis=2)
print(atoms.cell)
