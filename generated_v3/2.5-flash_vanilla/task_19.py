from ase import Atoms
import numpy as np

# CO2 분자 생성
# C는 원점, O는 양쪽 1.16 옹스트롬에 배치
co2 = Atoms('CO2',
            positions=[(0, 0, 0),
                       (1.16, 0, 0),
                       (-1.16, 0, 0)],
            cell=[10, 10, 10],
            pbc=False)

# 원자 간 거리 계산 및 출력
# C (인덱스 0), O1 (인덱스 1), O2 (인덱스 2)
dist_c_o1 = co2.get_distance(0, 1, mic=False)
dist_c_o2 = co2.get_distance(0, 2, mic=False)
dist_o1_o2 = co2.get_distance(1, 2, mic=False)

print(f"C-O1 거리: {dist_c_o1:.4f} Å")
print(f"C-O2 거리: {dist_c_o2:.4f} Å")
print(f"O1-O2 거리: {dist_o1_o2:.4f} Å")
