```python
import numpy as np
from ase.build import mx2

# MoS2 단층 구조 생성 (2H상)
# a: 격자 상수, thickness: S-S 층간 거리, vacuum: 진공층 두께
mos2_monolayer = mx2(formula='MoS2', kind='2H', a=3.16, thickness=3.12, vacuum=10.0)

# 2D 물질이므로 z축 방향의 주기성 제거
mos2_monolayer.pbc = (True, True, False)

# 생성된 구조의 cell 크기(격자 벡터) 출력
print("Cell vectors (in Angstrom):")
print(mos2_monolayer.cell)

# (선택) cell 매개변수 (a, b, c,
