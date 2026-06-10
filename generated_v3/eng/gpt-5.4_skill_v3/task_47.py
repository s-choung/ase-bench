from ase.build import bulk
from ase.calculators.emt import EMT
from ase.neighborlist import NeighborList, natural_cutoffs
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (3, 3, 3)
atoms.calc = EMT()

cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

counts = np.array([len(nl.get_neighbors(i)[0]) for i in range(len(atoms))])
print("Neighbors per atom:", counts.tolist())
print("Average coordination number:", counts.mean())
