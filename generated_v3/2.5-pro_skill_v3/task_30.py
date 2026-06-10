```python
import numpy as np
from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

# 1. Cu FCC 3x3x3 supercell 생성
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms = atoms.repeat((3, 3, 3))

# 2. 계산기 및 초기 속도 설정
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# 3. 초기 상태 출력
initial_volume = atoms.get_volume()
initial_pressure = -np.trace(atoms.get_stress(voigt=False)) / 3.0 / units.bar
print(f"Initial Volume: {initial_volume:.2f} Å^3")
print(f"Initial Pressure: {initial_pressure:.2f} bar")
print("-" * 30)

# 4. NPT MD 시뮬레이션 설정 및 실행
dyn = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature_K
