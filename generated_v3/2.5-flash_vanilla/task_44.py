```python
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
import numpy as np

# Cu(111) 4층 slab 생성
atoms = fcc111('Cu', size=(2, 2, 4), a=3.
