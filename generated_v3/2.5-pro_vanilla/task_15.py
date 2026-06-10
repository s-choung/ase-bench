from ase.build import fcc100, add_vacuum
from ase.calculators.emt import EMT

# Cu(100) 표면 생성: 3x3 유닛셀, 3개 원자층
# a=3.61은 Cu의 격자 상수
slab = fcc100('Cu', size=(3, 3, 3), a=3.61, orthogonal=True)

# z축 방향으로 12 옹스트롬의 진공층 추가
add_vacuum(slab, 12.0)

# ASE 내장 EMT 계산기 설정
slab.calc = EMT()

# 원자 수와 cell 정보 출력
print(f"Total number of atoms: {len(slab)}")
print("\nCell information (Angstrom):")
print(slab.cell)
