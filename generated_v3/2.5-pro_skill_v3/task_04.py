from ase.build import molecule
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# H2O 분자 구조 생성
atoms = molecule('H2O')

# EMT 계산기 설정
atoms.calc = EMT()

# 최적화 전 에너지 계산 및 출력
e_initial = atoms.get_potential_energy()
print(f"Initial potential energy: {e_initial:.4f} eV")

# BFGS를 이용한 구조 최적화 실행
optimizer = BFGS(atoms)
optimizer.run(fmax=0.05)

# 최적화 후 에너지 계산 및 출력
e_final = atoms.get_potential_energy()
print(f"Final potential energy:   {e_final:.4f} eV")
