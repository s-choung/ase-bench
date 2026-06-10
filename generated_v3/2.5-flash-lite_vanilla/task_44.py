from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms

# Cu(111) 4층 slab 생성
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

# 하부 2층 원자 선택 (tag 기반)
# slab.arrays['tags']는 각 원자의 tag를 저장합니다.
# 0부터 시작하므로, 하부 2층은 tag 0, 1에 해당하는 원자들입니다.
# 각 층은 2x2 격자이므로 4개의 원자로 구성됩니다.
# 따라서 tag 0: 0-3, tag 1: 4-7에 해당하는 원자들입니다.
# 여기서는 간단하게 tag를 직접 지정하는 대신, z 좌표를 기준으로 선택합니다.
# EMT 계산 시에는 tag가 자동으로 부여되지 않으므로, z 좌표를 이용하는 것이 일반적입니다.
# 만약 tag를 명시적으로 사용하고 싶다면, 원자 생성 시 tag를 부여해야 합니다.

# z 좌표를 기준으로 하부 2층 원자 선택
z_coords = slab.get_positions()[:, 2]
min_z = min(z_coords)
max_z = max(z_coords)
z_threshold = min_z + (max_z - min_z) / 2.0
indices_to_fix = [atom.index for atom in slab if atom.position[2] < z_threshold]

# FixAtoms constraint 설정
constraint = FixAtoms(indices=indices_to_fix)
slab.set_constraint(constraint)

# EMT calculator 설정
slab.calc = EMT()

# BFGS 최적화
optimizer = BFGS(slab)
optimizer.run()

# 최적화 전후 고정된 원자의 위치 비교
initial_positions = slab.get_positions()
fixed_indices_initial_pos = initial_positions[indices_to_fix]

final_positions = slab.get_positions()
fixed_indices_final_pos = final_positions[indices_to_fix]

print("Fixed atoms initial positions:")
print(fixed_indices_initial_pos)
print("\nFixed atoms final positions:")
print(fixed_indices_final_pos)

# 위치 변화가 없는지 확인
if (fixed_indices_initial_pos == fixed_indices_final_pos).all():
    print("\nFixed atoms positions did not change.")
else:
    print("\nFixed atoms positions changed (unexpected).")
