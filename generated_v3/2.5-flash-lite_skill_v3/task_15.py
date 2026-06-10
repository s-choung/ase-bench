from ase.build import fcc100
from ase.calculators.emt import EMT

# Cu(100) 표면 생성 (3x3, 3층, 12Å 진공)
atoms = fcc100('Cu', size=(3, 3, 3), vacuum=12.0)

# EMT 계산기 설정 (선택 사항이지만, 구조 최적화 등을 위해 필요할 수 있음)
atoms.calc = EMT()

# 원자 수 출력
print(f"Number of atoms: {len(atoms)}")

# Cell 정보 출력
print(f"Cell:\n{atoms.get_cell()}")
