from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.visualize import view

# MoS2 단층 구조 생성 (EMT calculator는 MoS2를 직접 지원하지 않으므로, 예시로 fcc111 사용)
# 실제 MoS2 구조를 위해서는 다른 빌더 함수나 외부 라이브러리 사용 필요
atoms = fcc111('Au', size=(2, 2, 1), vacuum=10.0)

# EMT calculator 할당 (예시용)
atoms.calc = EMT()

# Cell 크기 출력
print(atoms.cell)
