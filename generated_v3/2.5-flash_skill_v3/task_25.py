from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
import numpy as np

# 1. Cu FCC bulk 구조 생성 (초기 격자 상수 3.6 Å)
atoms = bulk('Cu', 'fcc', a=3.6)

# 2. EMT calculator 설정
atoms.calc = EMT()

# 3. 최적화 전 cell 크기와 에너지 출력
print("--- 최적화 전 ---")
print(f"Cell:\n{atoms.get_cell()}")
print(f"Lattice constant (a): {atoms.get_cell_lengths_and_angles()[0]:.4f} Å")
print(f"Potential Energy: {atoms.get_potential_energy():.4f} eV\n")

# 4. FrechetCellFilter를 사용하여 BFGS optimizer 설정
# FrechetCellFilter는 원자 위치와 셀을 동시에 최적화할 수 있도록 합니다.
opt = BFGS(FrechetCellFilter(atoms))

# 5. 최적화 실행 (fmax=0.01 eV/Å)
opt.run(fmax=0.01)

# 6. 최적화 후 cell 크기와 에너지 출력
print("--- 최적화 후 ---")
print(f"Cell:\n{atoms.get_cell()}")
print(f"Lattice constant (a): {atoms.get_cell_lengths_and_angles()[0]:.4f} Å")
print(f"Potential Energy: {atoms.get_potential_energy():.4f} eV")
