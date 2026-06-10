from ase.build import bulk
from ase.geometry import get_distances

atoms = bulk('Cu', 'fcc', a=3.6).repeat((2, 2, 2))
distances = get_distances(0, range(len(atoms)), mic=True, cell=atoms.cell)[1]
print(f"Minimum distance: {distances.min():.3f} Å")
print(f"Maximum distance: {distances.max():.3f} Å")
