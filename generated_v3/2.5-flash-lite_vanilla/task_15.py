from ase.build import fcc100
from ase.calculators.emt import EMT

# Cu(100) 표면 생성 (3층, 3x3 크기, 12Å 진공)
atoms = fcc100('Cu', size=(3, 3, 3), vacuum=12.0)

# EMT 계산기 할당 (내장 계산기 사용)
atoms.calc = EMT()

# 원자 수 및 cell 정보 출력
print(f"Number of atoms: {len(atoms)}")
print(f"Cell: {atoms.cell}")
