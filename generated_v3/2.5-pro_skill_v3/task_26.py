import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS
from ase.filters import FrechetCellFilter

# 1. Ni FCC bulk 구조 생성
atoms = bulk('Ni', 'fcc', a=3.5)

# 2. EMT calculator 설정
atoms.calc = EMT()

# 3. FrechetCellFilter를 사용하여 셀과 원자 위치 동시 최적화
filtered_atoms = FrechetCellFilter(atoms)

# 4. PreconLBFGS optimizer 설정
optimizer = PreconLBFGS(filtered_atoms, precon='auto')

# 5. 구조 최적화 실행
optimizer.run(fmax=0.01)

# 6. 결과 출력
steps = optimizer.get_number_of_steps()
final_energy = atoms.get_potential_energy()
cell_params = atoms.get_cell_lengths_and_angles()

print(f"Optimization converged in {steps} steps.")
print(f"Final potential energy: {final_energy:.4f} eV")
print(f"Final cell parameter (a): {cell_params[0]:.4f} Å")
