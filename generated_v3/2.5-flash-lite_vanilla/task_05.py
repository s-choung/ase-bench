from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Cu FCC bulk 생성 (EMT calculator 사용)
atoms = fcc111('Cu', size=(2, 2, 2), vacuum=10.0)
atoms.calc = EMT()

# 다양한 부피에서의 에너지 계산
volumes = []
energies = []
for scale in np.linspace(0.95, 1.05, 11):
    atoms.set_cell(atoms.cell * scale, scale_above_corners=True)
    atoms.positions *= scale
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

# EOS 피팅
eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()

# 결과 출력
print(f"평형 격자 상수 (부피): {v0:.4f} Å^3")
print(f"체적 탄성 계수: {B:.4f} GPa")
