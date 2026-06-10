from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs
from ase import units

# Cu FCC 3x3x3 supercell 생성
atoms = bulk('Cu', 'fcc', a=3.61, cubic=True)
atoms = atoms.repeat((3, 3, 3))

# natural_cutoffs를 사용하여 NeighborList 생성
cutoffs, _ = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

# 각 원자의 이웃 수 계산
num_neighbors = []
for i in range(len(atoms)):
    neighbors = nl.get_neighbors(i)[0]
    num_neighbors.append(len(neighbors))

# 평균 coordination number 계산 및 출력
avg_cn = sum(num_neighbors) / len(atoms)
print(f"Average coordination number: {avg_cn:.2f}")
