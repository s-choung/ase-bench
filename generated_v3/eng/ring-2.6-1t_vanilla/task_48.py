from ase.build import bulk
from ase.geometry import get_distances

atoms = bulk("Cu", "fcc", a=3.6, cubic=True) * (2, 2, 2)
d, _ = get_distances(0, atoms, mic=True)
d = d[1:]
print(f"Minimum distance: {d.min():.4f} Angstrom")
print(f"Maximum distance: {d.max():.4f} Angstrom")
