```python
import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

# 1. 시스템 설정
atoms = bulk('Cu', 'fcc', a=3.6) * (2, 2, 2)
atoms.calc = EMT()

# 2. 초기 속도 설정 (300K)
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# 3. Langevin MD 설정
dyn = Langevin(atoms, 5 * units.fs, temperature_K=300, friction=0.02)

# 4. 온도 램프 설정
total_steps = 200
temp_start = 300.0
temp_end = 600.0
temperatures = np.linspace(temp_start, temp_end, total_steps)

# 5. MD 시뮬레이션 실행
