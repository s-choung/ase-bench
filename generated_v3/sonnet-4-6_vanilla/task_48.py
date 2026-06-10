from ase.build import bulk
import numpy as np

cu = bulk('Cu', 'fcc', a=3.615) * (2, 2, 2)

distances = cu.get_distances(0, list(range(1, len(cu))), mic=True)

print(f"Number of atoms: {len(cu)}")
print(f"Min distance from atom 0: {distances.min():.4f} Å")
print(f"Max distance from atom 0: {distances.max():.4f} Å")
