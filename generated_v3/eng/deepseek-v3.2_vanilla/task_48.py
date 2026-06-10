from ase.build import bulk
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True).repeat((2, 2, 2))
pos0 = atoms.positions[0]
distances = atoms.get_distances(0, range(1, len(atoms)), mic=True)

print(f"Minimum distance: {np.min(distances):.4f} Å")
print(f"Maximum distance: {np.max(distances):.4f} Å")
