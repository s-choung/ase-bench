from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
import numpy as np

slab = fcc111('Cu', size=(3, 3, 4), vacuum=10.0)

# 태그: 하부 레이어부터 1,2,3,4 순서로 태그 부여
# fcc111에서 태그는 레이어 번호 (1=최하부)
for atom in slab:
    pass  # 태그 확인용

# 레이어별 태그 확인 및 하부 2층(tag 1,2) 고정
tags = slab.get_tags()
print("Tags assigned to atoms:", np.unique(tags))

fixed_indices = [atom.index for atom in slab if atom.tag in (1, 2)]
print(f"Fixed atom indices (tag 1,2): {fixed_indices}")

constraint = FixAtoms(indices=fixed_indices)
slab.set_constraint(constraint)

slab.calc = EMT()

# 최적화 전 고정 원자 좌표 저장
pos_before = slab.get_positions()[fixed_indices].copy()
print("\n=== Positions BEFORE optimization (fixed atoms) ===")
for idx, pos in zip(fixed_indices, pos_before):
    print(f"  Atom {idx:3d} (tag={slab[idx].tag}): {pos}")

opt = BFGS(slab, trajectory='cu111_opt.traj', logfile='cu111_opt.log')
opt.run(fmax=0.05)

# 최적화 후 고정 원자 좌표
pos_after = slab.get_positions()[fixed_indices].copy()
print("\n=== Positions AFTER optimization (fixed atoms) ===")
for idx, pos in zip(fixed_indices, pos_after):
    print(f"  Atom {idx:3d} (tag={slab[idx].tag}): {pos}")

# 변화량 비교
print("\n=== Position change (after - before) ===")
max_diff = 0.0
for idx, pb, pa in zip(fixed_indices, pos_before, pos_after):
    diff = pa - pb
    norm = np.linalg.norm(diff)
    max_diff = max(max_diff, norm)
    print(f"  Atom {idx:3d}: delta={diff}, |delta|={norm:.6e} Å")

print(f"\nMax displacement of fixed atoms: {max_diff:.6e} Å")
if max_diff < 1e-10:
    print("✓ Fixed atoms did NOT move (constraint working correctly).")
else:
    print("✗ Fixed atoms moved — check constraint setup.")
