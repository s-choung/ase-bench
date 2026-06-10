```python
import numpy as np
from ase import Atoms
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import BFGS

# 1. 초기 및 최종 상태 정의
initial = Atoms('Al3',
                positions=[(0, 0, 0),
                           (5, 0, 0),
                           (1.5, 0.5, 0)],
                cell=(10
