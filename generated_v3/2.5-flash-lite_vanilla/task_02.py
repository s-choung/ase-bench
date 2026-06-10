from ase import Atoms
from ase.calculators.emt import EMT
from ase.build import fcc111, add_adsorbate

# Pt(111) 4층 slab 생성
slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)

# CO 분자 생성
co = Atoms('CO', positions=[(0, 0, 0), (0, 0, 1.1)])

# CO 분자를 slab의 ontop 사이트에 흡착
add_adsorbate(slab, co, height=2.0, position=(0.5, 0.5))

# 최종 구조의 원자 수 출력
print(f"최종 구조의 원자 수: {len(slab)}")
