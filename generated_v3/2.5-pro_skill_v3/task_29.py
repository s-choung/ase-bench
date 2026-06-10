import numpy as np
from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# 1. 시스템 설정: Pd FCC 2x2x2 supercell
atoms = bulk('Pd', 'fcc', a=3.89, cubic=True)
atoms = atoms.repeat((2, 2, 2))

# 2. Calculator 설정
atoms.calc = EMT()

# 3. 초기 속도 설정 (500K)
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms) # Center-of-mass motion 제거

# 4. MD 시뮬레이션 전 총 에너지 계산
e_initial = atoms.get_total_energy()
print(f"Initial Total Energy: {e_initial:.4f} eV")

# 5. NVE MD 시뮬레이션 실행
dyn = VelocityVerlet(atoms, timestep=2 * units.fs)
dyn.run(200)

# 6. MD 시뮬레이션 후 총 에너지 계산 및 비교
e_final = atoms.get_total_energy()
print(f"Final Total Energy:   {e_final:.4f} eV")
print(f"Energy Difference:    {e_final - e_initial:.6f} eV")
