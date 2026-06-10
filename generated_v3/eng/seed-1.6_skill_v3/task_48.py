from ase.build import bulk
from ase.geometry import get_distances

atoms = bulk('Cu', 'fcc', a=3.6).repeat((2,2,2))
i, j = [0], range(1, len(atoms))
distances = get_distances(atoms.positions, atoms.cell, atoms.pbc, i, j, mic=True)[0].flatten()
print(f"Min distance: {min(distances):.3f} Å, Max distance: {max(distances):.3f} Å")
