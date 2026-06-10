from ase.build import bulk
from ase.geometry import get_distances

atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)

dists = get_distances(atoms.positions[0], atoms.positions[1:],
                      cell=atoms.cell, pbc=atoms.pbc, mic=True)

print(f"Minimum distance: {dists.min():.4f} Å")
print(f"Maximum distance: {dists.max():.4f} Å")
