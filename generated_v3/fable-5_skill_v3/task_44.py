import numpy as np
from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS

slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0)

# tag: 1=최상층, 4=최하층 → 하부 2층은 tag >= 3
mask = [atom.tag >= 3 for atom in slab]
fixed_idx = [i for i, m in enumerate(mask) if m]
slab.set_constraint(FixAtoms(mask=mask))

pos_before = slab.get_positions().copy()

slab.calc = EMT()
opt = BFGS(slab, trajectory='cu111_opt.traj')
opt.run(fmax=0.02)

pos_after = slab.get_positions()

print(f"고정 원자 수: {len(fixed_idx)} / 전체: {len(slab)}")
print("\n고정 원자 좌표 비교 (전 → 후, 변위):")
for i in fixed_idx:
    disp = np.linalg.norm(pos_after[i] - pos_before[i])
    print(f"  atom {i:2d} (tag={slab[i].tag}): "
          f"before {pos_before[i].round(4)} after {pos_after[i].round(4)} "
          f"|d|={disp:.2e} Å")

max_disp_fixed = np.max(np.linalg.norm(pos_after[fixed_idx] - pos_before[fixed_idx], axis=1))
free_idx = [i for i in range(len(slab)) if i not in fixed_idx]
max_disp_free = np.max(np.linalg.norm(pos_after[free_idx] - pos_before[free_idx], axis=1))

print(f"\n고정 원자 최대 변위: {max_disp_fixed:.2e} Å")
print(f"자유 원자 최대 변위: {max_disp_free:.4f} Å")
print("고정 원자 위치 불변:", np.allclose(pos_before[fixed_idx], pos_after[fixed_idx]))
