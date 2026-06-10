```python
from ase import Atoms

# CO2 분자 생성 (O-C-O)
# C 원자 (index 1)를 원점에, O 원자 (index 0, 2)를 양쪽에 배치
co2 = Atoms(symbols='OCO',
            positions=[[-1.16, 0, 0], [0, 0, 0], [1.16, 0, 0]],
            cell=[10, 10, 10],
            pbc=False)

# 모든 원자 쌍 사이의 거리를 계산하여 행렬로 반환
# distances[i, j]는
