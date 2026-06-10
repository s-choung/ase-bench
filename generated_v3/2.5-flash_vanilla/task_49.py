```python
from ase import build
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.optimize import BFGS
from ase.constraints import FixAtoms
import numpy as np

# --- 1. Cu FCC bulk의 격자상수를 EOS로 구하기 ---
# 초기 Cu FCC 벌크 구조 생성 (대략적인 격
