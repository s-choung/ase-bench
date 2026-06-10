from ase.build import bulk
from ase import Atoms

atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
dists = atoms.get_distances(0, range(1, len(atoms)), mic=True)

print(f"Number of atoms (excluding 0): {len(dists)}")
print(f"Minimum distance: {dists.min():.4f} Å")
print(f"Maximum distance: {dists.max():.4f} Å")
