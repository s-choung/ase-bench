from ase.build import fcc110, bcc110
from ase.calculators.emt import EMT
from ase.visualize import view

# BCC(110) 표면 생성
slab = bcc110('Fe', size=(2, 2, 4), vacuum=10.0)

# 원자 수 출력
print(f"Number of atoms: {len(slab)}")

# Cell 크기 출력
print(f"Cell dimensions: {slab.cell.lengths()}")

# EMT 계산기 할당 (GUI 함수는 사용하지 않음)
slab.calc = EMT()

# 결과 확인 (GUI 없이 콘솔 출력만)
print("Slab created and calculator assigned.")
