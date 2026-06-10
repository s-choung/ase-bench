```python
import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.units import GPa

# 1. 초기 구조 생성 및 계산기 설정
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# 2. 다양한 부피에 대한 에너지 계산
volumes = []
energies = []
cell = atoms.get_cell()
for x in np.linspace(0.95, 1.05, 11):
    atoms.set_cell(cell * x, scale_atoms=True)
    volumes.append(atoms.get_volume() / len(atoms))
    energies.append(atoms.get_potential_energy() / len(atoms))

# 3. Equation of State (EOS) 피팅 수행
eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()

# 4. 평형 격자상수 계산 (FCC: a^3 = 4 * V_
