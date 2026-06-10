import numpy as np
from ase.build import bulk

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)

indices = list(range(1, len(atoms)))
distances = atoms.get_distances(0, indices, mic=True)

print(f"원자 개수: {len(atoms)}")
print(f"최소 거리: {distances.min():.4f} Å")
print(f"최대 거리: {distances.max():.4f} Å")
