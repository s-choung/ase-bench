from ase.build import bcc110
from ase.calculators.emt import EMT

# Fe BCC(110) 표면 생성 (size=(2,2,4), vacuum=10 Å)
atoms = bcc110('Fe', size=(2, 2, 4), vacuum=10.0)

# 원자 수 출력
print(f"Number of atoms: {len(atoms)}")

# Cell 크기 출력
print(f"Cell dimensions: {atoms.get_cell().lengths()}")

# 계산기 설정 (EMT 사용 예시)
atoms.calc = EMT()
