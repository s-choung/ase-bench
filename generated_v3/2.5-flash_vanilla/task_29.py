from ase import build
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet
from ase import units

# 1. Pd FCC 2x2x2 supercell 생성
atoms = build.bulk('Pd', 'fcc', a=3.89) # Pd FCC 격자 상수 3.89 Å 사용
atoms = atoms * (2, 2, 2) # 2x2x2 supercell 생성

# 2. EMT calculator 설정
atoms.set_calculator(EMT())

# 3. 500K 초기 온도로 속도 설정
atoms.set_initial_velocities(temperature_K=500)

# 4. 초기 총 에너지 (운동 + 포텐셜) 계산
initial_kinetic_energy = atoms.get_kinetic_energy()
initial_potential_energy = atoms.get_potential_energy()
initial_total_energy = initial_kinetic_energy + initial_potential_energy

# 5. VelocityVerlet NVE MD 설정 (timestep 2fs)
timestep = 2 * units.fs
dyn = VelocityVerlet(atoms, timestep=timestep)

# 6. MD 시뮬레이션 200 스텝 실행
dyn.run(200)

# 7. 최종 총 에너지 (운동 + 포텐셜) 계산
final_kinetic_energy = atoms.get_kinetic_energy()
final_potential_energy = atoms.get_potential_energy()
final_total_energy = final_kinetic_energy + final_potential_energy

# 8. 초기 및 최종 총 에너지 차이 출력
energy_difference = final_total_energy - initial_total_energy
print(f"Initial Total Energy: {initial_total_energy:.4f} eV")
print(f"Final Total Energy: {final_total_energy:.4f} eV")
print(f"Total Energy Difference (Final - Initial): {energy_difference:.4f} eV")
