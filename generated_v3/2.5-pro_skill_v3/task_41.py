import os
from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.io import read

# 1. Cu FCC 벌크 구조 생성 및 EMT 계산기 설정
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

# 2. MD를 위한 초기 속도 설정
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# 3. NVE 앙상블에서 10 스텝 MD 실행 및 trajectory 저장
traj_file = 'cu_md.traj'
dyn = VelocityVerlet(atoms, 5 * units.fs, trajectory=traj_file)
dyn.run(10)

# 4. 저장된 trajectory 파일 읽기
images = read(traj_file, index=':')

# 5. 총 프레임 수와 마지막 프레임의 에너지 출력
total_frames = len(images)
last_energy = images[-1].get_potential_energy()

print(f"Total frames in trajectory: {total_frames}")
print(f"Potential energy of the last frame: {last_energy:.4f} eV")

# 생성된 파일 정리
os.remove(traj_file)
