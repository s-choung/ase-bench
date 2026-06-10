from ase.build import bulk
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.615) * (2, 2, 2)
distances = atoms.get_distances(0, range(1, len(atoms)), mic=True)

print(f"최소 거리: {distances.min():.4f} Å")
print(f"최대 거리: {distances.max():.4f} Å")
