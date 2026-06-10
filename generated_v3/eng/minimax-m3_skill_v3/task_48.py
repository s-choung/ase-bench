from ase.build import bulk
from ase.geometry import get_distances

atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
dists = get_distances(atoms[0].position, atoms.positions, cell=atoms.cell, pbc=True, mic=True)[1]
print(f"Min distance: {dists.min():.4f} Å")
print(f"Max distance: {dists.max():.4f} Å")
