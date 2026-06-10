import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.units import GPa

# 1. 초기 구조 설정
a0_guess = 4.09  # Ag의 실험 격자상수 (Å)
atoms = bulk('Ag', 'fcc', a=a0_guess)
atoms.calc = EMT()

# 2. 격자상수 변화에 따른 에너지 계산
volumes = []
energies = []
scales = np.linspace(0.95, 1.05, 7)

for scale in scales:
    lat = atoms.copy()
    lat.set_cell(atoms.cell * scale, scale_atoms=True)
    volumes.append(lat.get_volume())
    energies.append(lat.get_potential_energy())

# 3. Birch-Murnaghan EOS 피팅
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# 4. 결과 계산 및 출력
# v0 = a0^3 for a cubic cell
a0_fit = v0**(1/3.0)
B_gpa = B * (1.0 / GPa)

print(f"Equilibrium lattice constant (a0): {a0_fit:.4f} Å")
print(f"Bulk modulus (B): {B_gpa:.2f} GPa")
