```python
from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs
import numpy as np

# Cu FCC 3x3x3 supercell 생성
atoms = bulk('Cu', 'fcc', a=3.61)
atoms = atoms * (3, 3, 3)

# natural_cutoffs를 사용하여 NeighborList 생성
# natural_cutoffs는 각 원소에 대한 cutoff 리스트를 반환. Cu 단일 원소이므로 첫 번째 값 사용.
cutoff = natural_cutoffs(atoms)[0]
nl = NeighborList(cutoff, skin=0.0, self_interaction=False, bothways=True)
nl.update(atoms)

# 각 원자의 이웃 수 계산
coordination_numbers = []
for i in range(len(atoms)):
    indices, _ = nl.get_neighbors(i)
    coordination_numbers.append(len(indices))

# 평균 coordination number 출력
