from ase import bulk
from ase.calculators.emt import EMT
from ase.neighborlist import NeighborList, natural_cutoffs
import numpy as np

atoms = bulk("Cu", "fcc", a=3.6).repeat((3, 3, 3))
atoms.calc = EMT()
nl = NeighborList(natural_cutoffs(atoms), bothways=True, self_interaction=False)
nl.update(atoms)
coord_nums = [len(i) for i in nl.get_neighbors(0)]
print("Average CN:", np.mean(coord_nums))
