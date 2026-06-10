```python
from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms, FixBondLength
from ase.calculators.emt import EMT
from ase.optimize import BFGS
import numpy as np

# 1. Pt(111) 3층 slab 생성
# (2,2,3)은 2x2 표면 단위 셀에 3층을 의미합니다.
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

# 2. CO 분자 생성 및 흡착
# CO 분자 생성 (초기 C-O 거리 약 1.15 Å)
co = Atoms('CO', positions=[(0, 0, 0), (0, 0, 1.15)])

# CO를 slab 위에 흡착 (top site, Pt 원자 위)
# 흡착 높이 설정 (대략적인 값)
adsorption_height = 1.8

# slab의 가장 높은 Pt 원자의 z 좌표를 찾습니다.
top_pt_z = slab.positions[:, 2].max()

# CO를 흡착시킬 Pt 원자의 x, y 좌표를 찾습니다.
# 여기서는 slab의 첫 번째 표면 Pt 원자 위에 흡착시킵니다.
# (2,
