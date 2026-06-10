from ase.build import bulk
from ase.cell import Cell

# Al BCC bulk 구조 생성
# 격자상수 a=3.3 옹스트롬, cubic=True 설정
atoms = bulk('Al', 'bcc', a=3.3, cubic=True)

# cell과 chemical formula 출력
print("Unit Cell:")
print(atoms.cell)
print("\nChemical Formula:")
print(atoms.get_chemical_formula())
