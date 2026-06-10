from ase import build
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
import numpy as np

# Cu FCC bulk 초기 구조 설정
a0 = 3.61  # 초기 격자상수 추정치

# 격자상수 범위 설정 및 구조 생성
num_points = 7
delta_a = 0.05
a_values = np.linspace(a0 - delta_a, a0 + delta_a, num_points)

volumes = []
energies = []

# EMT 계산기 설정
calculator = EMT()

# 각 격자상수에 대해 에너지 계산
for a in a_values:
    cu = build.bulk('Cu', 'fcc', a=a)
    cu.set_calculator(calculator)
    energy = cu.get_potential_energy()
    volume = cu.get_volume()
    volumes.append(volume)
    energies.append(energy)

# Equation of State (EOS) 피팅
eos = EquationOfState(volumes, energies, eos_type='birchmurnaghan')
v0, e0, b0 = eos.fit()

# 평형 격자상수 계산 (FCC conventional cell: V = a^3)
a_eq = v0**(1/3)

# 체적탄성계수 단위를 GPa로 변환 (1 eV/Å^3 = 160.2176634 GPa)
b0_GPa = b0 * 160.2176634

# 결과 출력
print(f"평형 격자상수 (a_eq): {a_eq:.4f} Å")
print(f"평형 부피 (v0): {v0:.4f} Å^3")
print(f"체적탄성계수 (B0): {b0_GPa:.4f} GPa")
