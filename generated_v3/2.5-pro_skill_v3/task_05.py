import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units

# 1. 초기 Cu FCC 구조 생성 및 계산기 설정
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# 2. 다양한 부피에 대한 에너지 계산
cell = atoms.get_cell()
volumes = []
energies = []
for x in np.linspace(0.95, 1.05, 11):
    atoms_scaled = atoms.copy()
    atoms_scaled.set_cell(cell * x, scale_atoms=True)
    volumes.append(atoms_scaled.get_volume())
    energies.append(atoms_scaled.get_potential_energy())

# 3. Equation of State 피팅 수행
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# 4. 평형 격자상수 계산 (FCC: V = a^3)
a0 = v0**(1/3.0)

# 5. 결과 출력
print(f"Equilibrium volume (V₀): {v0:.2f} Å³")
print(f"Equilibrium lattice constant (a₀): {a0:.3f} Å")
print(f"Bulk modulus (B): {B / units.GPa:.1f} GPa")
