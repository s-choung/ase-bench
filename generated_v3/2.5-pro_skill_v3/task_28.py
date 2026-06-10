```python
import numpy as np
from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# 1. 구조 생성
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms = atoms.repeat((2, 2, 2))

# 2. Calculator 설정
atoms.calc = EMT()

# 3. MD 초기화 (300K)
T_start = 300.0
MaxwellBoltzmannDistribution(atoms, temperature_K=T_start)
Stationary(atoms)

# 4. Langevin Dynamics 설정
dyn = Langevin(atoms,
               timestep=5 * units.fs,
               temperature_K=T_start,
               friction=0.01 / units.fs)

# 5. Temperature Ramp 시뮬레이션
T_end = 600.0
total_steps = 200

print(f"Starting MD temperature ramp from {T_start} K to {T_end} K over {total_steps} steps.")

for i in range(total_steps):
    # 현재 스텝의 목표 온도 선형 보간
    current_target_T = T_start + (T_end - T_start) * i / (total_steps - 1)
    dyn.set_temperature(temperature_K=current_target_T)
    
    dyn.run(1)

    # 50 스텝마다 온도 출력
    if (i + 1) % 50 == 0:
        kinetic_T = atoms.get_temperature()
        print(f"Step: {i+1:4d}, Target T: {current_target_T:6.1f} K, Kinetic T: {kinetic_T:6.
