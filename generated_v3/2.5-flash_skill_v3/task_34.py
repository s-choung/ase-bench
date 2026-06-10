```python
from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.mep import NEB
from ase.io import write
import numpy as np

# 1. Cu(11
