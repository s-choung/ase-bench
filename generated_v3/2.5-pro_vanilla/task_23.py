```python
import numpy as np
from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT

# 1. Pt(111) 3층 slab 생성
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

# 2. OH 분자 생성 (O-H bond length ~0.97 Angstrom)
oh = Atoms('OH', positions=[(0, 0, 0), (0, 0, 0.97)])

# 3. 각 흡착 사이트 구조 생성
height = 1.8  # Pt-O 거리 (추정값)

# Ontop site
ontop_slab = slab.copy()
add_adsorbate(ontop_slab, oh, height, 'ontop')

# Bridge site
bridge_slab = slab.copy()
add_adsorbate(bridge_slab, oh, height, 'bridge')

# FCC hollow site
fcc_slab = slab.copy()
add_adsorbate(fcc_slab, oh, height, 'fcc')

# 4. 각 구조에 대해 에너지 계산 및 결과 저장
structures = {
    'ontop': ontop_slab,
    'bridge': bridge_slab,
    'fcc_hollow': fcc_slab
}
