from ase import Atoms
from ase.build import bulk

cu = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)
distances = cu.get_distances(0, range(len(cu)), mic=True)
print(min(distances[1:]), max(distances))
