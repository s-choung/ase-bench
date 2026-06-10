from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS
from ase.filters import FrechetCellFilter

# 1. Au FCC bulk 구조 생성 (초기 격자 상수 a=4.0)
atoms = bulk('Au', 'fcc', a=4.0, cubic=True)

# 2. EMT calculator 설정
atoms.calc = EMT()

# 3. 원자 위치와 셀을 동시에 최적화하기 위해 FrechetCellFilter 사용
ucf = FrechetCellFilter(atoms)

# 4. LBFGS optimizer 설정 및 실행
optimizer = LBFGS(ucf)
optimizer.run(fmax=0.01)

# 5. 결과 출력
final_energy = atoms.get_potential_energy()
steps = optimizer.nsteps

print(f"Optimization converged in {steps} steps.")
print(f"Final potential energy: {final_energy:.4f} eV")
