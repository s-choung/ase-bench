```python
import numpy as np
from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.npt import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

# Cu FCC 3x3x3 supercell 생성
atoms = bulk('Cu', 'fcc', a=3
