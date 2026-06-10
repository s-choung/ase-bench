from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# 1. Cu FCC bulk 구조 생성
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms = atoms.repeat((3, 3, 3)) # 더 큰 시스템으로 확장

# 2. EMT 계산기 설정
atoms.calc = EMT()

# 3. 초기 속도 설정 (300K)
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms) # 질량 중심 이동 제거

# 4. 초기 총 에너지 계산 및 출력
initial_total_energy = atoms.get_kinetic_energy() + atoms.get_potential_energy()
print(f"Initial Total Energy: {initial_total_energy:.4f} eV")

# 5. NVE (VelocityVerlet) MD 설정
timestep = 1 * units.fs # 1 fs
dyn = VelocityVerlet(atoms, timestep=timestep)

# 6. MD 시뮬레이션 실행 (50 스텝)
dyn.run(50)

# 7. 최종 총 에너지 계산 및 출력
final_total_energy = atoms.get_kinetic_energy() + atoms.get_potential_energy()
print(f"Final Total Energy: {final_total_energy:.4f} eV")
