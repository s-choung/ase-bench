from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import PreconLBFGS
from ase.constraints import FixAtoms
from ase.parallel import parprint

# Ni FCC bulk 생성
atoms = bulk('Ni', 'fcc', a=3.5)
atoms.calc = EMT()

# 구조 최적화 (PreconLBFGS 사용)
# 모든 원자를 고정하지 않기 위해 FixAtoms를 사용하지 않음
# PreconLBFGS는 기본적으로 모든 원자를 최적화 대상으로 함
optimizer = PreconLBFGS(atoms, precon='auto')

# 최적화 실행
max_steps = 10000
fmax = 0.01
optimizer.run(fmax=fmax, steps=max_steps)

# 결과 출력
final_energy = atoms.get_potential_energy()
cell_params = atoms.get_cell().cellpar()

parprint(f"Optimization finished.")
parprint(f"Number of steps: {optimizer.get_number_of_steps()}")
parprint(f"Final energy: {final_energy:.4f} eV")
parprint(f"Final cell parameters (a, b, c, alpha, beta, gamma): {cell_params}")
