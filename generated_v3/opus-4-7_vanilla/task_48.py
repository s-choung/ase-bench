from ase.build import bulk
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True).repeat((2, 2, 2))
distances = atoms.get_distances(0, range(1, len(atoms)), mic=True)
print("Min distance:", distances.min())
print("Max distance:", distances.max())
