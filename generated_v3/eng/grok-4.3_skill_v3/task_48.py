from ase.build import bulk
from ase.geometry import get_distances
atoms = bulk('Cu','fcc',a=3.6)*(2,2,2)
d = get_distances(atoms.positions[[0]], atoms.positions, atoms.cell, atoms.pbc, mic=True)[0][0]
print(min(d[d>0]), max(d))
