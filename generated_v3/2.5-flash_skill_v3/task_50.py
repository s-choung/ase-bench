```python
import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units

metal_data = {
    'Cu': {'initial_a': 3.6},
    'Ag': {'initial_a': 4.0},
    'Au': {'initial_
