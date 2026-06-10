from ase.build import bulk
from ase.geometry import get_distances

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms = atoms * (2, 2, 2)

distances, _ = get_distances(atoms[0].position, atoms.get_positions(), cell=atoms.get_cell(), pbc=True, mic=True)
distances = distances[1:]  # exclude self (0.0)

print(f"Min distance: {distances.min():.4f} Å")
print(f"Max distance: {distances.max():.4f} Å")
