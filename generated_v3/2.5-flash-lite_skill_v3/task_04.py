from ase import Atoms
from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# H2O 분자 생성
atoms = molecule('H2O')

# EMT 계산기 설정
atoms.calc = EMT()

# 최적화 전 에너지 계산 및 출력
energy_before = atoms.get_potential_energy()
print(f"에너지 (최적화 전): {energy_before:.4f} eV")

# BFGS 옵티마이저 설정
optimizer = BFGS(atoms)

# 구조 최적화 실행
optimizer.run(fmax=0.01)  # fmax: eV/Å

# 최적화 후 에너지 계산 및 출력
energy_after = atoms.get_potential_energy()
print(f"에너지 (최적화 후): {energy_after:.4f} eV")
