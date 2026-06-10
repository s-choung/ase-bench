from ase import build
from ase.calculators.emt import EMT

# Al BCC 구조 생성
# 격자상수 3.3 옹스트롬, cubic=True 설정
atoms = build.bulk('Al', 'bcc', a=3.3, cubic=True)

# EMT 계산기 할당 (요구사항에 따라 내장 계산기 사용)
atoms.calc = EMT()

# Cell 출력
print("Cell:")
print(atoms.get_cell())

# Chemical formula 출력
print("\nChemical Formula:")
print(atoms.get_chemical_formula())
