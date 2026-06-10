```python
import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

# Ag FCC bulk 구조 생성 (conventional cell, 4 atoms)
atoms = bulk('Ag', 'fcc', a=4.085) # Ag의 초기 격자상수 (Å)

# EMT calculator 설정
calculator = EMT()
atoms.set_calculator(calculator)

# 초기 격자상
