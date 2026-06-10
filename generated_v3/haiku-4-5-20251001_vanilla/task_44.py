from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
import numpy as np

# Cu(111) 4층 slab 생성
slab = fcc111('Cu', size=(4, 4, 4), a=3.61, vacuum=10.0)

# 원자 tag 설정 (z 좌표 기반으로 하부 2층 식별)
z_coords = slab.get_positions()[:, 2]
z_unique = np.unique(np.round(z_coords, 3))
z_unique.sort()

for i, atom in enumerate(slab):
    z = atom.position[2]
    layer = np.argmin(np.abs(z_unique - z))
    slab[i].tag = layer

# 하부 2층 고정
constraint = FixAtoms(tags=[0, 1])
slab.set_constraint(constraint)

# 최적화 전 좌표 저장
pos_before = slab.get_positions().copy()

# EMT calculator 설정 및 BFGS 최적화
slab.set_calculator(EMT())
dyn = BFGS(slab, trajectory='opt.traj')
dyn.run(fmax=0.01)

# 최적화 후 좌표
pos_after = slab.get_positions()

# 고정된 원자 좌표 비교
print("고정된 원자(tag 0, 1)의 좌표 변화:")
print("=" * 60)
for i, atom in enumerate(slab):
    if atom.tag in [0, 1]:
        diff = np.linalg.norm(pos_after[i] - pos_before[i])
        print(f"Atom {i} (tag={atom.tag}): 변위 = {diff:.2e} Å")

print("\n자유 원자(tag 2, 3)의 최대 변위:")
print("=" * 60)
max_disp = 0
for i, atom in enumerate(slab):
    if atom.tag in [2, 3]:
        diff = np.linalg.norm(pos_after[i] - pos_before[i])
        max_disp = max(max_disp, diff)
        if diff > 0.01:
            print(f"Atom {i} (tag={atom.tag}): 변위 = {diff:.4f} Å")

print(f"\n자유 원자 최대 변위: {max_disp:.4f} Å")
print(f"최종 에너지: {slab.get_potential_energy():.4f} eV")
