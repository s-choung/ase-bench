from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.neighbourlist import NeighborList
import numpy as np

atoms = fcc111('Cu', size=(3, 3, 3), vacuum=1.0)

nl = NeighborList(r=3.0, skin=False, natural_cutoffs=True)
nl.compute(atoms)

coordination_numbers = [len(neighbors) for neighbors in nl.get_neighbors()]
avg_coordination = np.mean(coordination_numbers)

print(f"Average Coordination Number: {avg_coordination}")
