from ase.build import fcc111, molecule, add_adsorbate

# Pt(111) 4층 slab 생성 (2x2 supercell)
slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)

# CO 분자 생성
co = molecule('CO')

# ontop 위치에 CO 흡착 (slab 객체가 직접 수정됨)
add_adsorbate(slab, co, height=1.8, position='ontop')

# 최종 구조의 총 원자 수 출력
print(len(slab))
