from ase import Atoms
from ase.build import bulk
from ase.geometry import get_distances

cu = bulk('Cu', 'fcc', a=3.6, cubic=True)
cu *= (2, 2, 2)
d = get_distances(0, cu.positions, cu.get_cell(), mic=True)
print(min(d[0][1:]), max(d[0][1:]))
