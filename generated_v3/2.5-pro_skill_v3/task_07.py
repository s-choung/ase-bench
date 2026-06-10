import numpy as np
from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# 1. Cu FCC 4x4x4 supercell 생성
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (4, 4, 4)
atoms.calc = EMT()

# 2. 300K 초기 속도 설정 및 COM 이동 제거
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# 3. 초기 총 에너지 계산 및 출력
e_pot_initial = atoms.get_potential_energy()
e_kin_initial = atoms.get_kinetic_energy()
e_total_initial = e_pot_initial + e_kin_initial
print(f"Initial Total Energy: {e_total_initial:.4f} eV")

# 4. NVE (VelocityVerlet) MD 50 스텝 실행
dyn = VelocityVerlet(atoms, timestep=1.0 * units.fs)
dyn.run(50)

# 5. 최종 총 에너지 계산 및 출력
e_pot_final = atoms.get_potential_energy()
e_kin_final = atoms.get_kinetic_energy()
e_total_final = e_pot_final + e_kin_final
print(f"Final Total Energy:   {e_total_final:.4f} eV")
