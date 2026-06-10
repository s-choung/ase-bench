from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS
from ase.constraints import FixAtoms

# Au FCC bulk 구조 생성
atoms = bulk('Au', 'fcc', a=4.08)  # 초기 격자 상수 설정 (EMT는 격자 상수에 민감하지 않음)

# EMT 계산기 설정
atoms.calc = EMT()

# 구조 최적화 (LBFGS)
optimizer = LBFGS(atoms)
optimizer.run(fmax=0.01)

# 최적화 스텝 수 및 최종 에너지 출력
print(f"Optimization steps: {optimizer.get_number_of_steps()}")
print(f"Final energy: {atoms.get_potential_energy()} eV")
