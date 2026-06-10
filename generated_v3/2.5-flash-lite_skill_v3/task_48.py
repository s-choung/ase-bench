from ase.build import bulk
from ase.neighborlist import NeighborList
from ase.geometry import get_distances
import numpy as np

# Cu FCC bulk 2x2x2 supercell 생성
atoms = bulk('Cu', 'fcc', a=3.61)
atoms = atoms.repeat((2, 2, 2))

# 0번 원자와 나머지 모든 원자 사이의 거리 계산 (주기 경계 조건 반영)
distances = get_distances(atoms, [0], range(1, len(atoms)), mic=True)

# 최소 거리와 최대 거리 계산 및 출력
min_distance = np.min(distances)
max_distance = np.max(distances)

print(f"Minimum distance from atom 0: {min_distance:.4f} Å")
print(f"Maximum distance from atom 0: {max_distance:.4f} Å")
