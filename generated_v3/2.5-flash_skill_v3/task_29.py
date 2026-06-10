from ase import Atoms, units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# 1. Pd FCC 2x2x2 supercell 생성
atoms = bulk('Pd', 'fcc', a=3.89)
atoms = atoms.repeat((2, 2, 2))

# 2. EMT calculator 설정
atoms.calc = EMT()

# 3. 초기 속도 설정 (500K) 및 COM 이동 제거
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# 4. 초기 총 에너지 기록
initial_kinetic_energy = atoms.get_kinetic_energy()
initial_potential_energy = atoms.get_potential_energy()
initial_total_energy = initial_kinetic_energy + initial_potential_energy

# 5. VelocityVerlet NVE MD 실행
md = VelocityVerlet(atoms, timestep=2 * units.fs)
md.run(200)

# 6. 최종 총 에너지 기록
final_kinetic_energy = atoms.get_kinetic_energy()
final_potential_energy = atoms.get_potential_energy()
final_total_energy = final_kinetic_energy + final_potential_energy

# 7. 에너지 보존 확인 출력
print(f"Initial Total Energy: {initial_total_energy:.4f} eV")
print(f"Final Total Energy:   {final_total_energy:.4f} eV")
print(f"Energy Difference:    {final_total_energy - initial_total_energy:.4f} eV")
