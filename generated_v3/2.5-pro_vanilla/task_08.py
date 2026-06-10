```python
import numpy as np
from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.vibrations import Vibrations

# 1. N2 분자 구조 생성
# 초기 추측값으로 N-N 결합 길이는 약 1.1 Å
n2 =
