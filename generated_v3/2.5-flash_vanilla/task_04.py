from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# H2O 분자 정의 (초기 대략적인 위치)
atoms = Atoms('H2O', positions=[(0, 0, 0), (0.9, 0, 0), (0, 0.9, 0)], cell=[3,3,3])

# EMT calculator 설정
atoms.set_calculator(EMT())

# 최적화 전 에너지 출력
initial_energy = atoms.get_potential_energy()
print(f"Initial energy: {initial_energy:.4f} eV")

# BFGS optimizer 설정 및 실행
optimizer = BFGS(atoms)
optimizer.run(fmax=0.01) # fmax는 최적화 종료 조건 (최대 힘)

# 최적화 후 에너지 출력
final_energy = atoms.get_potential_energy()
print(f"Final energy: {final_energy:.4f} eV")
