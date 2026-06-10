import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase import units

# Ag FCC bulk 생성
atoms = bulk('Ag', 'fcc', a=4.0)  # 초기 격자상수 설정 (실제 값과 다를 수 있음)
atoms.calc = EMT()

# 격자상수 변화 범위 설정 (±5%)
initial_cell = atoms.get_cell()
initial_volume = atoms.get_volume()
volumes = []
energies = []

for x in np.linspace(0.95, 1.05, 7):
    new_cell = initial_cell * x
    atoms.set_cell(new_cell, scale_atoms=True)
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

# Birch-Murnaghan EOS 피팅
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()

# 결과 출력 (GPa 단위 변환)
# v0: 평형 부피 (Å^3)
# B: Bulk Modulus (GPa)
# 평형 격자상수: v0의 세제곱근
equilibrium_lattice_constant = v0**(1/3)
bulk_modulus_GPa = B / units.GPa  # GPa 단위로 변환

print(f"평형 격자상수: {equilibrium_lattice_constant:.4f} Å")
print(f"Bulk Modulus: {bulk_modulus_GPa:.4f} GPa")
