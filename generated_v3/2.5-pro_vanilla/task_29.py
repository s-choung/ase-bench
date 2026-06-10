```python
import numpy as np
from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution

# 1. Pd FCC 2x2x2 supercell 생성
# bulk 함수를 사용하여 단위 셀을 만들고 repeat으로 확장
atoms = bulk('Pd', 'fcc', a=3.89, cubic=True).repeat((2, 2, 2))

# 2. ASE 내장 EMT calculator 설정
atoms.calc = EMT()

# 3. 500K 초기 온도 설정 (Maxwell-Boltzmann 분포)
MaxwellBoltzmannDistribution(atoms, temperature_K=500)

# 4. 초기 총 에너지 계산 및 출력
e_initial = atoms.get_total_energy()
print(f"Initial Total Energy: {e_initial:.5f} eV")

# 5. VelocityVerlet NVE MD 설정 (timestep: 2 fs)
dyn = VelocityVerlet(atoms, timestep=2 * units.fs)

# 6. MD 시뮬레이션 200 스텝 실행
dyn.run(200)

# 7. 최종 총 에너지 계산 및 출력
e_final = atoms.get_total_energy()
print(f"Final Total Energy:   {e_final:.5f} eV")

# 8. 에너지 보존 확인 (초기 에너지와 최종 에너지 차이)
energy_difference = e_final - e_initial
print(f"Energy Difference (Final -
