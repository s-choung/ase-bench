from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.md.velocitylimit import VelocityLimit
from ase.md.nve import NVE
from ase.md.verlet import VelocityVerlet
from ase.optimize import BFGS
from ase import units

# Cu FCC bulk 생성
atoms = fcc111('Cu', size=(2, 2, 2), vacuum=10.0)

# EMT calculator 설정
atoms.calc = EMT()

# 초기 온도 설정 및 속도 부여
atoms.set_temperature(300 * units.kB)

# 초기 총 에너지 계산
initial_energy = atoms.get_total_energy()
print(f"Initial total energy: {initial_energy:.4f} eV")

# Velocity Verlet MD 설정
dyn = VelocityVerlet(atoms, dt=0.001 * units.fs)

# MD 스텝 실행
for _ in range(50):
    dyn.run(1)

# 최종 총 에너지 계산
final_energy = atoms.get_total_energy()
print(f"Final total energy: {final_energy:.4f} eV")
