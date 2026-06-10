from ase.build import bulk
from ase.geometry import get_distances

atoms = bulk('Cu', 'fcc', a=3.6)
atoms = atoms.repeat((2, 2, 2))

p0 = atoms.positions[0]
distances, _ = get_distances(p0, atoms.positions, cell=atoms.cell, pbc=True)

print(f"Minimum distance: {distances.min():.4f} Å")
print(f"Maximum distance: {distances.max():.4f} Å")
