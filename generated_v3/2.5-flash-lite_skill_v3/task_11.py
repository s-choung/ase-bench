from ase.build import bulk
from ase.spacegroup import crystal

# Al BCC 구조 생성 및 격자 상수 설정
atoms = bulk('Al', 'bcc', a=3.3, cubic=True)

# 셀 정보 출력
print(f"Cell: {atoms.get_cell()}")

# 화학식 출력
print(f"Chemical Formula: {atoms.get_chemical_formula()}")
