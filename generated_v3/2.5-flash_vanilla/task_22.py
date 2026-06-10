```python
from ase import Atoms
from ase.build import fcc111, molecule
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
import numpy as np

# 1. Al(111) slab 생성 (3층, 2x2 표면 단위 셀)
# a는 Al의 격자 상수
a
