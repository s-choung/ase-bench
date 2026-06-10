from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs
from ase.calculators.emt import EMT

atoms = bulk('Cu', 'fcc') * (3, 3, 3)
atoms.calc = EMT()
cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)
n_neighbors = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]
avg_cn = sum(n_neighbors) / len(atoms)
print(f'Average coordination number: {avg_cn}')
