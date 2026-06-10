from ase.build import make_supercell
from ase.calculators.emt import EMT
from ase.neighborlist import NeighborList, natural_cutoffs
import numpy as np

atoms = make_supercell(EMT().get_default_atoms('Cu'), np.diag([3, 3, 3]))
atoms.calc = EMT()

cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

n_neighbors = np.array([len(nl.get_neighbors(i)[0]) for i in range(len(atoms))])
print(n_neighbors.mean())
