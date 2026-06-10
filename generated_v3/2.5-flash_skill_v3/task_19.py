from ase import Atoms
from ase.geometry import get_distances

# CO2 분자 생성
# C는 원점, O는 양쪽 1.16 옹스트롬에 배치
co2 = Atoms(
    symbols='CO2',
    positions=[(0, 0, 0), (1.16, 0, 0), (-1.16, 0, 0)],
    cell=(10, 10, 10),
    pbc=False
)

# 원자 간 거리 계산 및 출력
# C (index 0) - O (index 1)
distances_c_o1 = get_distances(co2, 0, 1)
print(f"Distance between C (0) and O (1): {distances_c_o1[0][0]:.2f} Å")

# C (index 0) - O (index 2)
distances_c_o2 = get_distances(co2, 0, 2)
print(f"Distance between C (0) and O (2): {distances_c_o2[0][0]:.2f} Å")

# O (index 1) - O (index 2)
distances_o_o = get_distances(co2, 1, 2)
print(f"Distance between O (1) and O (2): {distances_o_o[0][0]:.2f} Å")
