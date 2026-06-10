from ase.build import bulk
from ase.geometry import get_distances

atoms = bulk('Cu', 'fcc', a=3.615, cubic=True) * (2, 2, 2)

d, _ = get_distances(atoms.positions[0], atoms.positions[1:], cell=atoms.cell, pbc=atoms.pbc, mic=True)
distances = d.ravel()

print("min distance:", distances.min())
print("max distance:", distances.max())
