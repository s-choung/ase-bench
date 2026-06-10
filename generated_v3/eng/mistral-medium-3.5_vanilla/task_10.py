from ase.cluster import Octahedron
from ase import Atoms

cu = Octahedron('Cu', length=5)
print(len(cu), cu.positions.shape)
