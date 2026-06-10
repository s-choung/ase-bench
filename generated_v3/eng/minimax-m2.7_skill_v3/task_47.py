from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

atoms = bulk('Cu', 'fcc', a=3.61) * (3, 3, 3)
nl = NeighborList(natural_cutoffs(atoms), self_interaction=False)
nl.update(atoms)

coordination_numbers = []
for i in range(len(atoms)):
    nbr_indices, _ = nl.get_neighbors(i)
    coordination_numbers.append(len(nbr_indices))

avg_cn = sum(coordination_numbers) / len(atoms)
print(f"Total atoms: {len(atoms)}")
print(f"Average coordination number: {avg_cn:.2f}")
