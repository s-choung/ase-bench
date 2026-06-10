from ase import build
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.nvtbussi import NVTBussi
from ase import units

# Ag FCC 2x2x2 supercell 생성 (Ag 격자 상수 4.09 Å 사용)
atoms = build.bulk('Ag', 'fcc', a=4.09)
atoms = atoms * (2, 2, 2)

# EMT calculator 설정
atoms.set_calculator(EMT())

# 초기 속도를 500K Maxwell-Boltzmann 분포로 설정
MaxwellBoltzmannDistribution(atoms, temperature_K=500)

# NVT MD (Bussi thermostat) 설정
timestep = 5 * units.fs
temperature_K = 500
taut = 100 * units.fs # Thermostat coupling parameter

dyn = NVTBussi(atoms, timestep=timestep, temperature_K=temperature_K, taut=taut)

# 매 50스텝마다 온도를 출력하는 함수
def print_temperature():
    current_step = dyn.get_number_of_steps()
    current_temp = atoms.get_temperature()
    print(f"Step: {current_step}, Temperature: {current_temp:.2f} K")

# 함수를 MD 시뮬레이션에 연결
dyn.attach(print_temperature, interval=50)

# MD 시뮬레이션 실행
print("Starting NVT MD simulation...")
dyn.run(200)
print("Simulation finished.")
