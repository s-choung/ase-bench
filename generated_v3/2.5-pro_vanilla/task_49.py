```python
import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.constraints import FixAtoms
from ase.optimize import BFGS

# 1. EOS로 Cu bulk의 격자상수 계산
cu_bulk = bulk('Cu', 'fcc', a=3.6)
cu_bulk.calc = EMT()
cell = cu_bulk.get_cell()
volumes = []
energies = []
for x in np.linspace(0.95, 1.05, 11):
    cu_bulk.set_cell(cell * x, scale_atoms=True)
    volumes.append(cu_bulk.get_volume())
    energies.append(cu_bulk.get_potential_energy())

eos = EquationOfState(volumes, energies)
v
