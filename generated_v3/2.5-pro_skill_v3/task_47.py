import numpy as np
from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

# 1. Cu FCC 3x3x3 supercell 생성
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms = atoms.repeat((3, 3, 3))

# 2. natural_cutoffs를 사용하여 NeighborList 생성
cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

# 3. 각 원자의 이웃 수 계산
coordination_numbers = []
for i in range(len(atoms)):
    indices, offsets = nl.get_neighbors(i)
    coordination_numbers.append(len(indices))

# 4. 평균 coordination number 출력
average_cn = np.mean(coordination_numbers)
print(f"Average coordination number: {average_cn}")
