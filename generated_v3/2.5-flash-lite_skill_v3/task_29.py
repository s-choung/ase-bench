from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# 1. Pd FCC 2x2x2 supercell 생성
atoms = bulk('Pd', 'fcc', a=3.89, cubic=True)
atoms = atoms.repeat((2, 2, 2))

# 2. EMT calculator 설정
atoms.calc = EMT()

# 3. 초기 온도 설정 및 속도 부여 (NVE)
initial_temperature = 500  # K
MaxwellBoltzmannDistribution(atoms, temperature_K=initial_temperature)
Stationary(atoms)  # COM 속도 제거

# 4. VelocityVerlet MD 설정 (NVE)
timestep = 2 * units.fs
md_steps = 200
dyn = VelocityVerlet(atoms, timestep=timestep)

# 5. 초기 에너지 저장
initial_energy = atoms.get_total_energy()

# 6. MD 시뮬레이션 실행
dyn.run(md_steps)

# 7. 최종 에너지 저장
final_energy = atoms.get_total_energy()

# 8. 에너지 차이 출력
energy_difference = final_energy - initial_energy
print(f"Initial Total Energy: {initial_energy:.4f} eV")
print(f"Final Total Energy:   {final_energy:.4f} eV")
print(f"Energy Difference:    {energy_difference:.4f} eV")
