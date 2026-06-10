```python
from ase import Atoms
from ase.calculators.emt import EMT
from ase.neb import NEB
from ase.optimize import LBFGS

# Initial state: Al atoms at (0,0,0), (1,0,0), (4,0,0)
initial_positions = [
    (0.0, 0.0,
