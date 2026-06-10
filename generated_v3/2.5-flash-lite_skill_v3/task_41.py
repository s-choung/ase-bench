from ase import Atoms, units
from ase.calculators.emt import EMT
from ase.build import bulk
from ase.md.verlet import VelocityVerlet
from ase.io import read, write

# 1. Cu FCC bulk 생성 및 EMT calculator 설정
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# 2. MD 시뮬레이션 설정 및 실행
dt = 5 * units.fs
dyn = VelocityVerlet(atoms, timestep=dt)
traj_file = 'cu_md.traj'
write(traj_file, atoms)  # 첫 프레임 저장

for i in range(10):
    dyn.run(1)
    write(traj_file, atoms, append=True)

# 3. Trajectory 파일 읽기
read_atoms = read(traj_file, ':')

# 4. 총 프레임 수 및 마지막 프레임 에너지 출력
num_frames = len(read_atoms)
last_frame_energy = read_atoms[-1].get_potential_energy()

print(f"Total frames: {num_frames}")
print(f"Energy of the last frame: {last_frame_energy:.4f} eV")
