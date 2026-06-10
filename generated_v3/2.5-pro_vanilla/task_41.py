import os
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet
from ase import units
from ase.io import read

# 1. MD 시뮬레이션 설정 및 실행
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

dyn = VelocityVerlet(atoms, 5 * units.fs, trajectory='cu_md.traj')
dyn.run(10)

# 2. Trajectory 파일 읽기 및 분석
traj = read('cu_md.traj', index=':')
total_frames = len(traj)
last_frame_energy = traj[-1].get_potential_energy()

print(f"Total frames in trajectory: {total_frames}")
print(f"Potential energy of the last frame: {last_frame_energy:.4f} eV")

# 생성된 파일 정리
os.remove('cu_md.traj')
