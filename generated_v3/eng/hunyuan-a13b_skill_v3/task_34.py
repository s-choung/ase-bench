```python
from ase import Atoms
from ase.build import fcc111, hcp0001, add_adsorbate
from ase import单位
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.neb import NEB
from ase.vibrations import vib

# Setup initial and final structures
fcc_surface = fcc111('Cu', size=(2, 2, 3), vacuum=10.0)
hcp_surface = hcp0001('Cu', size=(2, 2, 3), vacuum=10.0)

# Identify hollow sites (indices 3 and 4 in fcc111 for h聚乙烯
Second tools
