import numpy as np
from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# 1. Cu(111) 4층 slab 생성
# fcc111은 자동으로 layer별 tag를 부여 (bottom layer tag=1)
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0, orthogonal=True)

# 2. 하부 2개 층(tag 1, 2) 고정
# tag가 3보다 작은 원자들을 고정하는 mask 생성
constraint_mask = [atom.tag < 3 for atom in slab]
slab.set_constraint(FixAtoms(mask=constraint_mask))

# 3. 최적화 전 고정된 원자의 좌표 저장
fixed_indices = [i for i, fixed in enumerate(constraint_mask) if fixed]
initial_fixed_positions = slab.get_positions()[fixed_indices].copy()
print(f"고정된 원자 수: {len(fixed_indices)}")
print(f"최적화 전 첫 번째 고정 원자(index {fixed_indices[0]}) 좌표:\n{initial_fixed_positions[0]}")

# 4. EMT calculator 설정 및 구조 최적화 수행
slab.calc = EMT()
optimizer = BFGS(slab, trajectory='cu111_opt.traj')
optimizer.run(fmax=0.05)

# 5. 최적화 후 좌표 비교
final_fixed_positions = slab.get_positions()[fixed_indices]
print(f"\n최적화 후 첫 번째 고정 원자(index {fixed_indices[0]}) 좌표:\n{final_fixed_positions[0]}")

# 6. 고정된 원자들의 위치가 변하지 않았는지 확인
positions_changed = not np.allclose(initial_fixed_positions, final_fixed_positions)
print(f"\n고정된 원자의 위치가 변경되었습니까? {positions_changed}")
if not positions_changed:
    print("FixAtoms 제약 조건이 성공적으로 적용되었습니다.")
