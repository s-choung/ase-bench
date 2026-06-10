import numpy as np
from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.geometry import get_distances

# 1. Cu FCC bulk 2x2x2 supercell 생성
# Cu FCC unit cell 생성
cu_unit_cell = bulk('Cu', 'fcc', a=3.61)

# 2x2x2 supercell 생성
atoms = cu_unit_cell * (2, 2, 2)

# 2. EMT calculator 설정 (거리 계산에는 필수 아니지만, 일반적인 ASE 워크플로우에 포함)
atoms.calc = EMT()

# 3. 0번 원자와 나머지 모든 원자 사이의 거리 계산 (mic=True)
# get_distances는 (distances, vectors) 튜플을 반환
distances_matrix, _ = get_distances(
    atoms[0].position,  # 0번 원자의 위치
    atoms.get_positions(),  # 모든 원자의 위치
    cell=atoms.get_cell(),
    pbc=atoms.get_pbc(),
    mic=True
)

# distances_matrix는 (1, N) 형태의 numpy 배열
# 0번 원자 자신과의 거리는 0이므로 제외하고 최소/최대 거리 찾기
distances = distances_matrix[0]
non_zero_distances = distances[distances > 1e-6] # 0에 가까운 값 제외

# 4. 최소 거리와 최대 거리 출력
if len(non_zero_distances) > 0:
    min_distance = np.min(non_zero_distances)
    max_distance = np.max(non_zero_distances)
    print(f"Minimum distance from atom 0 to other atoms: {min_distance:.4f} Å")
    print(f"Maximum distance from atom 0 to other atoms: {max_distance:.4f} Å")
else:
    print("No other atoms found to calculate distances.")
