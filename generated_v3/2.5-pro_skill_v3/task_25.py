import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

# 1. 초기 구조 생성 및 계산기 설정
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

# 2. 최적화 전 상태 출력
initial_energy = atoms.get_potential_energy()
initial_cell = atoms.get_cell()
print("--- Before Optimization ---")
print(f"Potential Energy: {initial_energy:.4f} eV")
print(f"Cell vectors:\n{initial_cell}")
print(f"Lattice constant: {initial_cell[0, 0]:.4f} Å")

# 3. 셀과 원자 위치 동시 최적화
cell_filter = FrechetCellFilter(atoms)
optimizer = BFGS(cell_filter)
optimizer.run(fmax=0.01)

# 4. 최적화 후 상태 출력
final_energy = atoms.get_potential_energy()
final_cell = atoms.get_cell()
print("\n--- After Optimization ---")
print(f"Potential Energy: {final_energy:.4f} eV")
print(f"Cell vectors:\n{final_cell}")
print(f"Lattice constant: {final_cell[0, 0]:.4f} Å")
