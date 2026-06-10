```python
import numpy as np
from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen

# 1. 시스템 설정: Cu FCC 3x3x3 supercell
atoms = bulk('Cu', 'fcc', a=3.61) * (3, 3, 3)
atoms.calc = EMT()

#
