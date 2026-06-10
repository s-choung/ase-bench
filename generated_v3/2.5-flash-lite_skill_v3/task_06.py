from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# 1. Cu FCC bulk 2x2x2 supercell 생성
atoms = bulk('Cu', 'fcc', a=3.61)  # Cu FCC 기본 격자 상수
atoms = atoms.repeat((2, 2, 2))   # 2x2x2 슈퍼셀 생성

# 2. EMT 계산기 설정
atoms.calc = EMT()

# 3. 초기 온도 설정 및 속도 분포
temperature = 300.0 * units.kB  # 300K를 에너지 단위로 변환
MaxwellBoltzmannDistribution(atoms, temperature_K=300.0)
Stationary(atoms)  # COM 속도 제거

# 4. 초기 온도 및 에너지 저장
initial_temperature = atoms.get_temperature()
initial_energy = atoms.get_potential_energy()

# 5. Langevin MD 설정
timestep = 5 * units.fs
friction = 0.01 / units.fs  # 마찰 계수 (예시 값)
md_steps = 100

langevin_md = Langevin(atoms, timestep=timestep, temperature_K=300.0, friction=friction)

# 6. MD 실행
langevin_md.run(md_steps)

# 7. 최종 온도 및 에너지 저장
final_temperature = atoms.get_temperature()
final_energy = atoms.get_potential_energy()

# 8. 결과 출력
print(f"Initial Temperature: {initial_temperature:.2f} K")
print(f"Initial Energy: {initial_energy:.4f} eV")
print(f"Final Temperature: {final_temperature:.2f} K")
print(f"Final Energy: {final_energy:.4f} eV")
