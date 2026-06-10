```python
import numpy as np
from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.npt import NPTBerendsen

# 1. 시스템 설정
atoms = bulk('Al', 'fcc', a=4.05)
atoms = atoms * (2, 2, 2)
