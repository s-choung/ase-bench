from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# H2O 분자 생성
atoms = molecule('H2O')

# EMT calculator 설정
atoms.calc = EMT()

# 최적화 전 에너지 계산 및 출력
initial_energy = atoms.get_potential_energy()
print(f"Initial energy: {initial_energy:.4f} eV")

# BFGS optimizer 설정 및 구조 최적화
optimizer = BFGS(atoms)
optimizer.run()

# 최적화 후 에너지 계산 및 출력
final_energy = atoms.get_potential_energy()
print(f"Final energy: {final_energy:.4f} eV")
