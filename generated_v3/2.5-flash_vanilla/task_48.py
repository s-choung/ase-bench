from ase.build import bulk
from ase.calculators.emt import EMT
import numpy as np

# Cu FCC bulk 구조 생성 (표준 격자 상수 사용)
a_cu = 3.61  # Angstroms
atoms = bulk('Cu', 'fcc', a=a_cu)

# 2x2x2 supercell 생성
atoms = atoms * (2, 2, 2)

# ASE 내장 calculator 설정 (EMT 예시, get_distances에는 필수 아님)
atoms.calc = EMT()

# 0번 원자와 모든 다른 원자 사이의 거리 계산 (mic=True로 주기 경계 조건 반영)
# get_distances(a, b, mic=True)는 a 원자에서 b 원자들까지의 거리를 반환
distances = atoms.get_distances(0, range(len(atoms)), mic=True)

# 최소 거리와 최대 거리 계산
# 0번 원자 자신과의 거리는 0이므로, 최소 거리는 0보다 큰 값 중에서 찾음
min_distance = np.min(distances[distances > 0])
max_distance = np.max(distances)

# 결과 출력
print(f"Minimum distance from atom 0: {min_distance:.4f} Å")
print(f"Maximum distance from atom 0: {max_distance:.4f} Å")
