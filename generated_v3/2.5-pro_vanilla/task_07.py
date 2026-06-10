import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.units import Kelvin, fs

# 1. 시스템 설정: 4x4x4 Cu FCC supercell
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms = atoms.repeat((4, 4, 4))

# 2. Calculator 설정: EMT (Effective Medium Theory)
atoms.calc = EMT()

# 3. 초기 온도 설정: 300K
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# 4. 초기 총 에너지 계산 및 출력
epot_initial = atoms.get_potential_energy()
ekin_initial = atoms.get_kinetic_energy()
etot_initial = epot_initial + ekin_initial
print(f"Initial total energy: {etot_initial:.5f} eV")

# 5. NVE MD 시뮬레이션 설정 및 실행
dyn = VelocityVerlet(atoms, timestep=1.0 * fs)
dyn.run(50) # 50 스텝 실행

# 6. 최종 총 에너지 계산 및 출력
epot_final = atoms.get_potential_energy()
ekin_final = atoms.get_kinetic_energy()
etot_final = epot_final + ekin_final
print(f"Final total energy:   {etot_final:.5f} eV")
