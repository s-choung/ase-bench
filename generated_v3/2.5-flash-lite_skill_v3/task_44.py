from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
import numpy as np

# 1. Cu(111) 4층 slab 생성
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

# 2. 하부 2층 원자 tag 설정 (0-indexed)
# 각 층은 4개의 원자로 구성 (size=(2,2))
# 층 0: tag 0-3
# 층 1: tag 4-7
# 층 2: tag 8-11
# 층 3: tag 12-15
# 하부 2층은 tag 0-7
for atom in slab:
    if atom.tag < 8:
        atom.tag = 1  # 고정할 원자 tag를 1로 설정
    else:
        atom.tag = 0  # 고정하지 않을 원자 tag를 0으로 설정

# 3. FixAtoms constraint 설정
constraint = FixAtoms(mask=[atom.tag > 0 for atom in slab])
slab.set_constraint(constraint)

# 4. EMT calculator 설정
slab.calc = EMT()

# 5. 최적화 전 원자 좌표 저장
initial_positions = slab.get_positions()

# 6. BFGS 구조 최적화 수행
optimizer = BFGS(slab)
optimizer.run(fmax=0.05)

# 7. 최적화 후 원자 좌표 저장
final_positions = slab.get_positions()

# 8. 고정된 원자의 위치 비교 출력
print("--- Fixed Atom Positions Comparison ---")
fixed_indices = [atom.index for atom in slab if atom.tag > 0]

for idx in fixed_indices:
    initial_pos = initial_positions[idx]
    final_pos = final_positions[idx]
    if not np.allclose(initial_pos, final_pos):
        print(f"Warning: Fixed atom {idx} position changed!")
    print(f"Atom {idx}: Initial={initial_pos}, Final={final_pos}")

print("\nOptimization finished.")
