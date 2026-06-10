from ase.build import mx2
from ase.visualize import view

# MoS2 단층 구조 생성
mos2_slab = mx2('MoS2', kind='2H', a=3.18, thickness=3.17, vacuum=10.0)

# 셀 크기 출력
print(mos2_slab.get_cell())

# (선택 사항) 구조 확인
# view(mos2_slab)
