import numpy as np
from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# 1. Al 2x2x2 FCC supercell 생성
atoms = bulk('Al', 'fcc', a=4.05, cubic=True)
atoms = atoms.repeat((2, 2, 2))

# 2. EMT 계산기 설정
atoms.calc = EMT()

# 3. MD 시뮬레이션 파라미터 설정
temperature_K = 500.0
pressure_GPa = 10.0
pressure_eV_per_A3 = pressure_GPa * units.GPa  # 단위 변환

# 4. 초기 속도 분포 설정 및 질량중심 고정
MaxwellBoltzmannDistribution(atoms, temperature_K=temperature_K)
Stationary(atoms)

# 5. 초기 부피 출력
initial_volume = atoms.get_volume()
print(f"Initial volume: {initial_volume:.2f} A^3")

# 6. NPT MD 시뮬레이터 생성 및 실행
dyn = NPTBerendsen(
    atoms,
    timestep=2.0 * units.fs,
    temperature_K=temperature_K,
    pressure_au=pressure_eV_per_A3,
    taut=100 * units.fs,
    taup=1000 * units.fs,
)
dyn.run(100)

# 7. 최종 부피 출력
final_volume = atoms.get_volume()
print(f"Final volume: {final_volume:.2f} A^3")
