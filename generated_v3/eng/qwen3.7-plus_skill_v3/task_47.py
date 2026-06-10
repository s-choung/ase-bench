from ase.build import bulk
from ase.calculators.emt import EMT
from ase.neighborlist import natural_cutoffs, NeighborList

atoms = bulk('Cu', 'fcc', a=3.6)
atoms = atoms.repeat((3, 3, 3))
atoms.calc = EMT()

cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

num_neighbors = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]
avg_cn = sum(num_neighbors) / len(atoms)

print(f"Average coordination number: {avg_cn:.2f}")
