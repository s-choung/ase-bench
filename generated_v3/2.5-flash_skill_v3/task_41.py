```python
from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.io import read, Trajectory

# 1. Cu FCC bulk 구조 생성
atoms = bulk('Cu', 'fcc', a
