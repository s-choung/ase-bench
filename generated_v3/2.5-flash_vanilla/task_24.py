from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

# Au FCC bulk 구조 생성
atoms = bulk('Au', 'fcc', a=4.08)

# EMT calculator 설정
atoms.set_calculator(EMT())

# LBFGS optimizer 설정
optimizer = LBFGS(atoms)

# 최적화 step 수를 세기 위한 콜백 함수
step_count = 0
def count_steps():
    global step_count
    step_count += 1

optimizer.attach(count_steps, interval=1)

# 구조 최적화 실행 (fmax=0.01)
optimizer.run(fmax=0.01)

# 최적화 step 수와 최종 에너지 출력
print(f"Optimization steps: {step_count}")
print(f"Final energy: {atoms.get_potential_energy():.4f} eV")
