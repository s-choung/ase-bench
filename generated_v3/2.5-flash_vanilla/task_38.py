```python
from ase import build
from ase.calculators.emt import EMT
from ase.optimize import LBFGS
from ase.constraints import ExpCellFilter
from ase.phonons import Phonons
from ase.thermochemistry import HarmonicThermo
import numpy as np

# 1. Cu bulk 구조 생성 및 EMT calculator 설정
# 초기 격자 상수 (Cu
