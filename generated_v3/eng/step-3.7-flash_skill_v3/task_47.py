from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

atoms = bulk('Cu', 'fcc', a=3.6).repeat((3, 3, 3))
cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

coordination_numbers = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]
average_cn = sum(coordination_numbers) / len(atoms)
print(f"Average coordination number: {average_cn:.2f}")
