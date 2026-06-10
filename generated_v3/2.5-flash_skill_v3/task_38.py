from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

# Cu bulk 구조 생성 (primitive cell)
atoms = bulk('Cu', 'fcc', a=3.6, cubic=False)

# EMT calculator 설정
atoms.calc = EMT()

# 구조 최적화 (셀과 원자 위치 모두)
opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

# 최적화된 구조의 포텐셜 에너지
potential_energy = atoms.get_potential_energy()

# 진동 주파수 계산
vib = Vibrations(atoms, name='cu_bulk_vib')
vib.run()
vib_energies = vib.get_energies() # eV 단위

# HarmonicThermo를 사용하여 Helmholtz 자유 에너지 계산
thermo = HarmonicThermo(vib_energies=vib_energies, potentialenergy=potential_energy)
helmholtz_energy_300K = thermo.get_helmholtz_energy(temperature=300)

# 결과 출력 (eV 단위)
print(f"{helmholtz_energy_300K:.4f}")

# 계산 후 생성된 파일 정리
vib.clean()
