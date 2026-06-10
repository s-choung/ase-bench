from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Cu FCC 2x2x2 supercell 생성
atoms = bulk('Cu', 'fcc', a=3.61, cubic=True)
atoms = atoms.repeat((2, 2, 2))
atoms.calc = EMT()

# 초기 온도 설정 (300K)
temperature_start = 300.0 * units.kB
temperature_end = 600.0 * units.kB
total_steps = 200
timestep = 5 * units.fs

# 초기 속도 분포 설정
MaxwellBoltzmannDistribution(atoms, temperature=temperature_start)
Stationary(atoms)

# Langevin MD 설정
md = Langevin(atoms, timestep=timestep, temperature=temperature_start, friction=0.01 / units.fs)

# Temperature ramp 구현
for step in range(total_steps):
    # 온도 업데이트 (선형 증가)
    current_temp = temperature_start + (temperature_end - temperature_start) * step / total_steps
    md.set_temperature(current_temp)

    # MD 스텝 실행
    md.run(1)

    # 매 50 스텝마다 온도 출력
    if (step + 1) % 50 == 0:
        print(f"Step: {step + 1}, Temperature: {atoms.get_temperature() / units.kB:.2f} K")

print("MD simulation finished.")
