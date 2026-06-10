from ase.build import bulk
from ase.geometry import get_distances

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)

dists, _ = get_distances(atoms.positions[0], atoms.positions[1:], cell=atoms.cell, pbc=True, mic=True)
dists = dists.ravel()

print(dists.min(), dists.max())
