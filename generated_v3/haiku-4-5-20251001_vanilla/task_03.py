from ase.build import bulk
from ase.lattice.cubic import Diamond
import numpy as np

# MoS2 단층 구조 생성
a = 3.18  # MoS2 격자상수 (앙스트롬)
c = 3.17  # Mo-S 층 두께

# MoS2 단층 구조 수동 생성
atoms_list = []
# Mo 원자
atoms_list.append(['Mo', 0, 0, 0])
# S 원자 (위아래)
atoms_list.append(['S', a/3, 2*a/3, c/2])
atoms_list.append(['S', 2*a/3, a/3, -c/2])

from ase import Atoms

positions = np.array([[0, 0, 0],
                      [a/3, 2*a/3, c/2],
                      [2*a/3, a/3, -c/2]])

symbols = ['Mo', 'S', 'S']

mos2 = Atoms(symbols, positions=positions)

# 셀 설정 (육각형 셀)
cell = np.array([[a, 0, 0],
                 [-a/2, a*np.sqrt(3)/2, 0],
                 [0, 0, c + 10.0]])  # 진공 10 옹스트롬 추가

mos2.set_cell(cell)
mos2.center(vacuum=5, axis=2)  # z축 중심 정렬

# 셀 크기 출력
print("Cell parameters (Å):")
print(f"a = {mos2.cell[0, 0]:.4f}")
print(f"b = {mos2.cell[1, 1]:.4f}")
print(f"c = {mos2.cell[2, 2]:.4f}")
print(f"\nCell volume: {mos2.get_volume():.4f} Ų")
print(f"\nAtomic positions:")
print(mos2.get_positions())
