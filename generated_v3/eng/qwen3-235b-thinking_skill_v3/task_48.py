from ase.build import bulk
from ase.geometry import get_distances

atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
D = get_distances([atoms.positions[0]], atoms.positions, cell=atoms.cell, pbc=atoms.pbc)[0][0]
dists = D[1:]
print(min(dists), max(dists))
