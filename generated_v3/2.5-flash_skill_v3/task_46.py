```python
from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms, FixBondLength

# Pt(111) 3층 slab 생성
slab = fcc111('Pt', size=(2,
