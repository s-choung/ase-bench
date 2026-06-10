from ase.build import bulk
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.61, cubic=True).repeat((2, 2, 2))
d = atoms.get_distances(0, range(len(atoms)), mic=True)
print(np.min(d), np.max(d))
