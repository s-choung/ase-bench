from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import PreconLBFGS

# Ni FCC 구조 생성 (초기 lattice constant = 3.5 Å)
atoms = bulk('Ni', 'fcc', a=3.5)

# EMT calculator 설정
atoms.calc = EMT()

# PreconLBFGS optimizer 설정 (precon='auto')
# cell과 원자 위치를 모두 최적화
opt = PreconLBFGS(atoms, precon='auto')

# 구조 최적화 실행 (fmax < 0.01 eV/Å)
opt.run(fmax=0.01)

# 결과 출력
print(f"Optimization steps: {opt.nsteps}")
print(f"Final potential energy: {atoms.get_potential_energy():.4f} eV")
print(f"Final cell parameter (a): {atoms.get_cell().lengths()[0]:.4f} Å")
