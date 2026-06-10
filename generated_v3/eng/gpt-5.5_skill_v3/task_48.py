from ase.build import bulk
from ase.geometry import get_distances

atoms = bulk("Cu", "fcc", a=3.6, cubic=True) * (2, 2, 2)

_, distances = get_distances(
    atoms.positions[0:1],
    atoms.positions[1:],
    cell=atoms.cell,
    pbc=atoms.pbc,
    mic=True,
)

distances = distances.ravel()
print("Minimum distance:", distances.min())
print("Maximum distance:", distances.max())
