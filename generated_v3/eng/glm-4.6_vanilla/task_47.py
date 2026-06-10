from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

atoms = bulk('Cu', 'fcc', a=3.615).repeat((3, 3, 3))
cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

coordination_numbers = []
for i in range(len(atoms)):
    indices, offsets = nl.get_neighbors(i)
    coordination_numbers.append(len(indices))

avg_coordination = sum(coordination_numbers) / len(coordination_numbers)
print(f"Average coordination number: {avg_coordination:.2f}")
