```python
import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

# 1. 초기 Cu FCC 구조 생성 (최적값과 다른 격자상수로 시작)
atoms = bulk('Cu', 'fcc', a=3.5, cubic=True)
atoms.calc = EMT()

# 2. 최적화 전 상태 출력
print("Before optimization:")
initial_a = atoms.cell.lengths()[0]
initial_energy = atoms.get_potential_energy()
print(f"  Cell
