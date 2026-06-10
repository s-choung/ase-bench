from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import LBFGS

# Au FCC bulk 구조 생성 (2x2x2 단위 셀)
atoms = fcc111('Au', size=(2, 2, 2), vacuum=10.0)

# EMT 계산기 설정
atoms.calc = EMT()

# LBFGS 옵티마이저 설정
optimizer = LBFGS(atoms, trajectory='au_fcc.traj', logfile='au_fcc.log')

# 구조 최적화 실행 (fmax=0.01)
optimizer.run(fmax=0.01)

# 최적화 후 최종 에너지 출력
print(f"Final energy: {atoms.get_potential_energy()}")
