from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# 1. Cu FCC bulk 생성 및 계산기 설정
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# 2. 초기 속도 설정 (300K)
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)  # COM 속도 제거

# 3. 초기 총 에너지 저장
initial_energy = atoms.get_total_energy()
print(f"Initial Total Energy: {initial_energy:.4f} eV")

# 4. NVE MD 설정 (VelocityVerlet)
timestep = 5 * units.fs
md = VelocityVerlet(atoms, timestep=timestep)

# 5. MD 실행 (50 스텝)
n_steps = 50
for _ in range(n_steps):
    md.step()

# 6. 최종 총 에너지 저장 및 출력
final_energy = atoms.get_total_energy()
print(f"Final Total Energy:   {final_energy:.4f} eV")

# 7. 에너지 보존 확인 (간단한 출력)
energy_diff = final_energy - initial_energy
print(f"Energy Difference:    {energy_diff:.4f} eV")
