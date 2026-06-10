from ase.build import bulk
from ase.geometry import get_distances

atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
p1 = atoms.positions[0:1]
p2 = atoms.positions[1:]
distances = get_distances(p1, p2, cell=atoms.cell, pbc=atoms.pbc, mic=True)[1]
print(f"Min distance: {distances.min():.3f} Å")
print(f"Max distance: {distances.max():.3f} Å")
