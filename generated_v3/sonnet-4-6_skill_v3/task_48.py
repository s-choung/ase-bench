import numpy as np
from ase.build import bulk
from ase.geometry import get_distances

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)

positions = atoms.get_positions()
cell = atoms.get_cell()
pbc = atoms.get_pbc()

D, d = get_distances(positions[0:1], positions[1:], cell=cell, pbc=pbc)

distances = d[0]

print(f"총 원자 수: {len(atoms)}")
print(f"최소 거리: {distances.min():.4f} Å")
print(f"최대 거리: {distances.max():.4f} Å")
