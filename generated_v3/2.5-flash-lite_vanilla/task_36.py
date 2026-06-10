from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.eos import calculate_eos
from ase.optimize import BFGS
import numpy as np

# Ag FCC bulk 생성
atoms = fcc111('Ag', size=(2, 2, 2), vacuum=10.0)
atoms.calc = EMT()

# 격자상수 변화 범위 설정
a0 = atoms.get_cell()[0, 0]
a_range = np.linspace(a0 * 0.95, a0 * 1.05, 7)

# 에너지 계산
energies = []
for a in a_range:
    atoms.set_cell([a, a, a, 90, 90, 90])
    atoms.set_positions(atoms.get_scaled_positions() * a / a0)
    atoms.get_calculator().reset()
    energies.append(atoms.get_total_energy())

# Birch-Murnaghan EOS 피팅
eos = calculate_eos(atoms, a_range, energies)
v0, e0, B = eos.fit()

# 결과 출력 (GPa 단위 변환)
print(f"Equilibrium lattice constant: {v0**(1/3):.3f} Angstrom")
print(f"Bulk modulus: {B / 10.0:.3f} GPa")
