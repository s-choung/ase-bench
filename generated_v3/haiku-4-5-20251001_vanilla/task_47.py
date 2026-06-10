from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

cu = bulk('Cu', 'fcc', a=3.61, cubic=True)
cu = cu.repeat((3, 3, 3))

cutoffs = natural_cutoffs(cu)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.build(cu)

coordination_numbers = [len(nl.get_neighbors(i)[0]) for i in range(len(cu))]
avg_cn = sum(coordination_numbers) / len(coordination_numbers)

print(f"Average Coordination Number: {avg_cn:.2f}")
print(f"Min CN: {min(coordination_numbers)}, Max CN: {max(coordination_numbers)}")
