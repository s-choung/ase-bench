```python
from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import LBFGS
from ase.io import write
import numpy as np

# 1. Cu(111) 표면 생성
# 3x
