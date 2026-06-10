import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# 1. Cu 벌크 구조 생성 및 계산기 설정
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

# 2. 구조 최적화 (셀 및 원자 위치)
opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=1e-4)

# 3. 진동 분석 수행
# 최적화된 구조의 0K 포텐셜 에너지를 저장
potential_energy = atoms.get_potential_energy()

vib = Vibrations(atoms, name='vib_cu')
vib.run()
vib_energies = vib.get_energies()
vib.clean()

# 4. HarmonicThermo를 사용하여 Helmholtz 자유에너지 계산
# vib_energies: 진동 에너지 (eV)
# potentialenergy: 0K에서의 전자 에너지 (eV)
thermo = HarmonicThermo(vib_energies=vib_energies,
                        potentialenergy=potential_energy)

# 300K에서의 Helmholtz 자유에너지 (F = E_pot + F_vib)
helmholtz_energy_300K = thermo.get_helmholtz_energy(temperature=300)

# 5. 결과 출력
print(f"Optimized Potential Energy (E_pot): {potential_energy:.4f} eV")
print(f"Helmholtz Free Energy at 300 K (F): {helmholtz_energy_300K:.4f} eV")
