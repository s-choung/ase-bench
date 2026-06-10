from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.bussi import Bussi
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# 1. Ag FCC 2x2x2 supercell 생성
atoms = bulk('Ag', 'fcc', a=4.09)  # Ag FCC 격자 상수 (대략적인 값)
atoms = atoms * (2, 2, 2)          # 2x2x2 supercell 생성

# 2. EMT calculator 설정
atoms.calc = EMT()

# 3. 초기 속도 설정 (500K) 및 COM 이동 제거
temperature_K = 500
MaxwellBoltzmannDistribution(atoms, temperature_K=temperature_K)
Stationary(atoms)

# 4. Bussi thermostat NVT MD 설정
timestep_fs = 5
md_steps = 200
log_interval = 50

dyn = Bussi(atoms, timestep=timestep_fs * units.fs, temperature_K=temperature_K)

# 5. 매 50스텝마다 온도 기록 및 출력
def print_temperature():
    current_step = dyn.get_number_of_steps()
    current_temp = atoms.get_temperature()
    print(f"Step: {current_step}, Temperature: {current_temp:.2f} K")

dyn.attach(print_temperature, interval=log_interval)

# MD 시뮬레이션 실행
print(f"Starting NVT MD simulation for Ag at {temperature_K} K for {md_steps} steps...")
dyn.run(md_steps)
print("MD simulation finished.")
