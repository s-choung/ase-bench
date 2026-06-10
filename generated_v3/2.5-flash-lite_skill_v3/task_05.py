from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Cu FCC 벌크 생성
atoms = bulk('Cu', 'fcc', a=3.6)  # 초기 격자 상수
atoms.calc = EMT()

# 다양한 부피에서의 에너지 계산
cell = atoms.get_cell()
volumes = []
energies = []
for x in np.linspace(0.95, 1.05, 11):  # 5% 범위에서 11개 포인트
    atoms.set_cell(cell * x, scale_atoms=True)
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

# Equation of State 피팅
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# 결과 출력
print(f"평형 격자 상수 (a): {np.sqrt(v0 / 4):.4f} Å")
print(f"평형 부피 (V0): {v0:.4f} Å³")
print(f"체적 탄성 계수 (B): {B:.4f} GPa")
