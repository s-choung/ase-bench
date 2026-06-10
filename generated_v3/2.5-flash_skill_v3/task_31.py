```python
from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# 1. Al FCC 2x2x2 supercell 생성
atoms = bulk('Al', 'f
