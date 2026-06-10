from ase.build import mx2
from ase.calculators.emt import EMT

# MoS2 단층 구조 생성 (a=3.16 옹스트롬, 10 옹스트롬 진공 추가)
atoms = mx2(name='MoS2', kind='2H', a=3.16, layers=1, vacuum=10)

# EMT (Embedded Atom Model) 계산기 설정
atoms.calc = EMT()

# 셀 크기 출력 (a, b, c 길이)
print(atoms.get_cell().lengths())
