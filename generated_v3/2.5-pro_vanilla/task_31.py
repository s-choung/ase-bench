```python
import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase import units

# 1. Al FCC 2x2x2 supercell 생성
atoms = bulk('Al', 'fcc', a=4.05) * (2, 2, 2)
atoms.calc = EMT()

# 2. 초기 부피 출력
initial_volume = atoms.get_volume()
print(f"Initial volume: {initial_volume:.2f} A^3")
