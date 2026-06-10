from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.io import read, write

# Cu FCC bulk 생성
from ase.build import fcc111
atoms = fcc111('Cu', size=(2, 2, 2), vacuum=10.0)

# EMT calculator 설정
atoms.calc = EMT()

# MD 설정
dyn = Langevin(atoms, timestep=1.0, temperature=300.0, friction=0.1)

# MD 실행 및 trajectory 저장
trajectory_file = 'cu_fcc_emt.traj'
for _ in range(10):
    dyn.run(1)
    write(trajectory_file, atoms, append=True)

# Trajectory 파일 읽기
traj = read(trajectory_file, ':')

# 총 프레임 수 출력
print(f"Total frames: {len(traj)}")

# 마지막 프레임의 에너지 출력
print(f"Energy of the last frame: {traj[-1].get_total_energy()}")
