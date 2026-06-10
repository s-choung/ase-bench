from ase.build import bulk
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.615, cubic=True) * (2, 2, 2)

i = 0
indices = np.arange(len(atoms))
indices = indices[indices != i]

d = atoms.get_distances(i, indices, mic=True)

print(d)
print(d.min())
print(d.max())
