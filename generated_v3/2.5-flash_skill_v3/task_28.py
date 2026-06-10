```python
from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.io.trajectory import Trajectory

# 1. Cu FCC 2x2x2 supercell 생성
atoms
