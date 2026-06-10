import numpy as np
from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

# 1. Cu FCC bulk 구조 생성 (초기 격자 상수 추정치)
initial_a = 3.6  # Cu FCC의 대략적인 격자 상수
atoms = bulk('Cu', 'fcc', a=initial_a, cubic=True)

# 2. EMT 계산기 설정
atoms.calc = EMT()

# 3. 다양한 부피에 대한 에너지 계산
cell = atoms.get_cell()
volumes = []
energies = []

# 격자 상수를 0.95배에서 1.05배까지 변화시키며 에너지 계산
for x in np.linspace(0.95, 1.05, 11): # 11개의 스케일 팩터
    a_scaled = atoms.copy()
    a_scaled.set_cell(cell * x, scale_atoms=True) # 셀 크기 변경 및 원자 위치 스케일링
    
    volumes.append(a_scaled.get_volume())
    energies.append(a_scaled.get_potential_energy())

# 4. Equation of State (EOS) 피팅
# Birch-Murnaghan EOS 사용
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# 5. 평형 격자 상수 계산
# FCC 단위 셀의 부피 V = a^3 이므로, a = V^(1/3)
a0 = v0**(1/3)

# 6. 결과 출력
print(f"평형 격자 상수 (a0): {a0:.3f} Å")
print(f"평형 부피 (V0): {v0:.3f} Å³")
print(f"체적 탄성 계수 (Bulk Modulus, B): {B / 1.0e9:.3f} GPa") # eV/Å³를 GPa로 변환 (1 eV/Å³ = 160.21766 GPa)
