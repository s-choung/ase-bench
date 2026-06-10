import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# 1. Ag FCC 2x2x2 supercell 생성
atoms = bulk('Ag', 'fcc', a=4.09, cubic=True)
atoms = atoms.repeat((2, 2, 2))

# 2. Calculator 설정
atoms.calc = EMT()

# 3. 500K 초기 속도 설정 및 COM 모션 제거
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# 4. Bussi thermostat NVT MD 설정
dyn = Bussi(atoms, timestep=5*units.fs, temperature_K=500)

# 5. MD 실행 및 50 스텝마다 온도 출력
print(f"Step {'Temperature (K)':>18}")
print("-" * 25)

for i in range(4):
    dyn.run(50)
    step = (i + 1) * 50
    temperature = atoms.get_temperature()
    print(f"{step:4d} {temperature:18.2f}")
