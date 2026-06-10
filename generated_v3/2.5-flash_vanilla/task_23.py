```python
from ase import Atoms
from ase.build import fcc111, add_vacuum
from ase.calculators.emt import EMT
import numpy as np

# 1. Pt(111) 3-layer slab 생성
# 2x2 표면 단위 셀, 3층, 10 옹스트롬 진공층
