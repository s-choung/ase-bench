from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import CalculateEOS
import numpy as np

# Ag FCC bulk 생성
ag = bulk('Ag', 'fcc', a=4.085)
ag.calc = EMT()

# 격자상수 범위 설정 (±5%)
a0 = ag.cell[0, 0]
strain_range = np.linspace(0.95, 1.05, 7)
lattice_constants = a0 * strain_range

# EOS 계산
eos = CalculateEOS(ag, trajectory='ag_eos.traj')
v, e, B = eos.fit()

# 결과 출력
print(f"평형 격자상수: {eos.a0:.4f} Å")
print(f"Bulk Modulus: {eos.B / 1e9:.2f} GPa")
