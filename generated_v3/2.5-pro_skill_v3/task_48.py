import numpy as np
from ase.build import bulk

# 1. Cu FCC 2x2x2 supercell 생성
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms = atoms.repeat((2, 2, 2))

# 2. 0번 원자와 나머지 모든 원자 사이의 거리 계산 (주기 경계 조건 적용)
# atoms.get_distances(a, b, mic=True)는 a 원자와 b 원자들 사이의 거리를 계산
# a는 단일 인덱스, b는 인덱스 시퀀스
distances = atoms.get_distances(0, range(1, len(atoms)), mic=True)

# 3. 최소 및 최대 거리 찾기
min_distance = np.min(distances)
max_distance = np.max(distances)

# 4. 결과 출력
print(f"Total number of atoms: {len(atoms)}")
print(f"Minimum distance from atom 0 (mic=True): {min_distance:.4f} Å")
print(f"Maximum distance from atom 0 (mic=True): {max_distance:.4f} Å")
