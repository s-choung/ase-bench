from ase import Atoms
from ase.geometry import get_distances
import numpy as np

# CO2 분자 생성: C(0,0,0), O(+/-1.16, 0, 0)
co2 = Atoms(symbols=['C', 'O', 'O'],
            positions=[[0.0, 0.0, 0.0],
                       [1.16, 0.0, 0.0],
                       [-1.16, 0.0, 0.0]],
            cell=[10, 10, 10],
            pbc=False)

# 원자 간 거리 계산 (거리 행렬)
# get_distances는 (distances, distance_vectors) 튜플을 반환
dist_matrix, _ = get_distances(co2.get_positions())

# 결과 출력
print("CO2 Positions (Å):")
print(co2.get_positions())
print("\nInteratomic distance matrix (Å):")
# 보기 좋게 소수점 3자리까지 포맷팅
with np.printoptions(precision=3, suppress=True):
    print(dist_matrix)
