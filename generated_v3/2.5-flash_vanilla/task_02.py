```python
from ase.build import fcc111, molecule
from ase.calculators.emt import EMT
import numpy as np

# Pt lattice constant
a_pt = 3.92

# 1. Pt(111) 4-layer slab 생성
# size=(2,2,4)는 2x2 단위 셀에 4
