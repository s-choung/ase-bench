from ase.build import bulk
from ase.calculators.emt import EMT

# Al BCC 구조 생성 및 격자 상수 설정
a = 3.3
atoms = bulk('Al', 'bcc', a=a)

# EMT 계산기 할당 (GUI 함수 사용 안 함)
atoms.calc = EMT()

# cell과 chemical formula 출력
print(atoms.cell)
print(atoms.get_chemical_formula())
