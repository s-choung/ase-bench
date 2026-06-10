from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.units import fs, kB
import numpy as np

# Ag FCC 2x2x2 supercell 생성
atoms = bulk('Ag', 'fcc', a=4.09, cubic=True)
atoms = atoms.repeat((2, 2, 2))

# Calculator 설정
atoms.calc = EMT()

# 초기 속도 설정 (500K)
T = 500  # Kelvin
MaxwellBoltzmannDistribution(atoms, temperature_K=T, use_masses=True)
Stationary(atoms)  # COM 속도 제거

# Bussi thermostat으로 NVT MD 설정
dt = 5 * fs
friction = 0.01 / fs  # Bussi thermostat의 마찰 계수 (예시 값)
thermostat = Bussi(atoms, timestep=dt, temperature_K=T, friction=friction)

# MD 실행 및 온도 기록
nsteps = 200
print_interval = 50

for step in range(nsteps):
    thermostat.step()
    if (step + 1) % print_interval == 0:
        current_temp = atoms.get_temperature()
        print(f"Step {step + 1}/{nsteps}, Temperature: {current_temp:.2f} K")
