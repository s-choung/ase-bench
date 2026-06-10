from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase import units
from ase.io.trajectory import Trajectory

# Cu FCC 3x3x3 supercell 생성
atoms = bulk('Cu', 'fcc', a=3.61, cubic=True)
atoms = atoms.repeat((3, 3, 3))

# EMT 계산기 설정
atoms.calc = EMT()

# 초기 셀 볼륨 및 압력 저장
initial_volume = atoms.get_volume()
initial_pressure = atoms.get_calculator().get_pressure()

# NPT Berendsen MD 설정
md = NPTBerendsen(
    atoms=atoms,
    timestep=5 * units.fs,
    temperature_K=300,
    taut=100 * units.fs,
    taup=1000 * units.fs,
)

# Trajectory 파일 설정 (선택 사항)
traj = Trajectory('npt_md.traj', 'w', atoms)
md.attach(traj.write, interval=1)

# MD 실행 (200 스텝)
md.run(200)
traj.close()

# 최종 셀 볼륨 및 압력 저장
final_volume = atoms.get_volume()
final_pressure = atoms.get_calculator().get_pressure()

# 결과 출력
print(f"Initial Cell Volume: {initial_volume:.2f} Å³")
print(f"Initial Pressure: {initial_pressure:.2f} bar")
print(f"Final Cell Volume: {final_volume:.2f} Å³")
print(f"Final Pressure: {final_pressure:.2f} bar")
