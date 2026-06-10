from ase.build import mx2, add_vacuum

# MoS2 단층 구조 생성 (2H-MoS2, 기본 격자 상수 사용)
mos2 = mx2('MoS2', kind='2H')

# z 방향으로 10 옹스트롬 진공 추가 (in-place 수정)
add_vacuum(mos2, 10)

# 최종 cell 크기 출력
print(mos2.get_cell())
