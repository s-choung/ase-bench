```python
from ase.build import fcc111
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
import numpy as np

# 1. Cu(111) 4층 slab 생성
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0, orthogonal=True)

# 2. 하부 2개 층에 tag=0, 상부 2개 층에 tag=1 할당
# z 좌표를 기준으로 층을 구분
unique_z = sorted(np.unique(slab.get_positions()[:, 2]))
bottom_layers_z_cutoff = unique_z[1] 

tags = np.where(slab.positions[:, 2] <= bottom_layers_z_cutoff, 0, 1)
slab.set_tags(tags)

# 3. tag=0 인 원자들을 고정
constraint = FixAtoms(mask=(slab.get_tags() == 0))
slab.set_constraint(constraint)

# 4. EMT calculator 설정
slab.calc = EMT()

# 5. 최적화 전 고정된 원자들의 좌표 저장 및 출력
fixed_indices = np.where(slab
