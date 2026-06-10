from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT

# Pt(111) 4층 slab 생성
slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)

# CO 분자 생성
co = molecule('CO')

# CO 분자를 slab의 ontop 사이트에 흡착
add_adsorbate(slab, co, height=1.8, position='ontop')

# 최종 구조의 원자 수 출력
print(len(slab))
