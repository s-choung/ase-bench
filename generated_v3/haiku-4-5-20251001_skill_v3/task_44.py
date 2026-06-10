from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
import numpy as np

# Cu(111) 4층 slab 생성
atoms = fcc111('Cu', size=(3, 3, 4), vacuum=10.0, a=3.61)

# tag 설정: 하부 2층은 tag=1, 상부 2층은 tag=0
z_coords = atoms.get_positions()[:, 2]
z_sorted = np.sort(np.unique(z_coords))
z_threshold = z_sorted[1]  # 2번째 층의 z 좌표

for atom in atoms:
    if atom.position[2] <= z_threshold:
        atom.tag = 1
    else:
        atom.tag = 0

# 고정할 원자 인덱스 (tag=1)
fixed_indices = [atom.index for atom in atoms if atom.tag == 1]
print(f"고정된 원자 인덱스: {fixed_indices}")

# 최적화 전 고정된 원자의 좌표
pos_before = atoms.get_positions()[fixed_indices].copy()
print(f"\n최적화 전 고정된 원자 좌표:\n{pos_before}")

# FixAtoms 제약 조건 적용
atoms.set_constraint(FixAtoms(indices=fixed_indices))

# EMT calculator 설정 및 BFGS 최적화
atoms.calc = EMT()
opt = BFGS(atoms, trajectory='opt.traj')
opt.run(fmax=0.05)

# 최적화 후 고정된 원자의 좌표
pos_after = atoms.get_positions()[fixed_indices].copy()
print(f"\n최적화 후 고정된 원자 좌표:\n{pos_after}")

# 좌표 변화 확인
coord_diff = np.max(np.abs(pos_after - pos_before))
print(f"\n고정된 원자 좌표 최대 변화: {coord_diff:.2e} Å")
print(f"좌표 변화 없음: {coord_diff < 1e-10}")

# 전체 원자 에너지
print(f"\n최적화된 구조 에너지: {atoms.get_potential_energy():.4f} eV")
