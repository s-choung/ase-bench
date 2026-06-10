from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

# 1. Au FCC bulk 구조 생성
atoms = bulk('Au', 'fcc', a=4.0, cubic=True)

# 2. EMT calculator 설정
atoms.calc = EMT()

# 3. LBFGS optimizer를 사용한 구조 최적화
dyn = LBFGS(atoms)
dyn.run(fmax=0.01)

# 4. 결과 출력
print(f"Optimization steps: {dyn.nsteps}")
print(f"Final energy: {atoms.get_potential_energy():.4f} eV")
