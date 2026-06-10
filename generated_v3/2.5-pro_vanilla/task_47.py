```python
import numpy as np
from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

# 1. Cu FCC 3x3x3 supercell 생성
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (3, 3, 3)

# 2. natural_cutoffs를 사용하여 NeighborList 생성
cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
