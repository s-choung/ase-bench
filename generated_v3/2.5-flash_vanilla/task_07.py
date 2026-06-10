from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

# Cu FCC bulk 3x3x3 supercell 생성
atoms = bulk('Cu', 'fcc', a=3.61, cubic=True) * (3, 3, 3)

# EMT calculator 설정
atoms.set_calculator(EMT())

# 초기 온도 300K 설정 및 속도 할당
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# 초기 총 에너지 계산 및 출력
initial_total_energy = atoms.get_total_energy()
print(f"Initial Total Energy: {initial_total_energy:.4f} eV")

# NVE (VelocityVerlet) MD 설정 (dt=1 fs)
dyn = VelocityVerlet(atoms, dt=1.0 * units.fs)

# 50 스텝 MD 실행
dyn.run(50)

# 최종 총 에너지 계산 및 출력
final_total_energy = atoms.get_total_energy()
print(f"Final Total Energy: {final_total_energy:.4f} eV")
