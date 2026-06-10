from ase.build import surface
from ase.calculators.emt import EMT

# Cu(100) 표면 생성
# size=(3,3,1)은 표면의 x, y 방향으로 3x3 단위 셀을 의미하며,
# layers=3은 표면이 3개 층으로 구성됨을 의미합니다.
# vacuum=12는 표면 위에 12 옹스트롬의 진공 공간을 추가합니다.
atoms = surface('Cu', (1, 0, 0), layers=3, vacuum=12.0, size=(3, 3, 1))

# EMT 계산기 할당 (계산은 수행하지 않음)
atoms.calc = EMT()

# 원자 수와 셀 정보 출력
print(f"Number of atoms: {atoms.get_number_of_atoms()}")
print(f"Cell information:\n{atoms.get_cell()}")
