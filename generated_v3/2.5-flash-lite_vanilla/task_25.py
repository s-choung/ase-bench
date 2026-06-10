from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.filters import FrechetCellFilter

# Cu FCC bulk 생성 (예시로 2x2x2 단위 셀 사용)
atoms = fcc111('Cu', size=(2, 2, 2), vacuum=10.0)

# EMT 계산기 설정
atoms.calc = EMT()

# 초기 셀 크기와 에너지 출력
print(f"Initial cell: {atoms.cell}")
print(f"Initial energy: {atoms.get_total_energy()}")

# FrechetCellFilter와 BFGS 옵티마이저 설정
optimizer = BFGS(atoms, trajectory='cu_fcc_opt.traj')
optimizer.attach(FrechetCellFilter(atoms, dx=0.001), interval=1)
optimizer.attach(FixAtoms(indices=[atom.index for atom in atoms if atom.tag == 1]), interval=1) # 표면 원자 고정 (필요시 수정)

# 최적화 수행 (fmax=0.01)
optimizer.run(fmax=0.01)

# 최적화 후 셀 크기와 에너지 출력
print(f"Optimized cell: {atoms.cell}")
print(f"Optimized energy: {atoms.get_total_energy()}")
