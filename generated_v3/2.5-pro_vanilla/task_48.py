import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT

# 1. Cu FCC 2x2x2 supercell 생성
atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()

# 2. 0번 원자와 모든 원자 사이의 거리 계산 (주기 경계 조건 적용)
distances = atoms.get_distances(0, range(len(atoms)), mic=True)

# 3. 자기 자신과의 거리(0)를 제외한 거리들 필터링
non_zero_distances = distances[distances > 1e-9]

# 4. 최소/최대 거리 계산 및 출력
min_dist = np.min(non_zero_distances)
max_dist = np.max(non_zero_distances)

print(f"0번 원자로부터의 최소 거리: {min_dist:.4f} Å")
print(f"0번 원자로부터의 최대 거리: {max_dist:.4f} Å")
