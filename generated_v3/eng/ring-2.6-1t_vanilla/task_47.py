from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.neighborlist import NeighborList, natural_cutoffs
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (3, 3, 3)

cutoffs = natural_cutoffs(atoms, mult=1.1)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

coordinations = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]
avg_cn = np.mean(coordinations)

for i, cn in enumerate(coordinations):
    print(f"Atom {i}: {cn} neighbors")

print(f"\nAverage coordination number: {avg_cn:.2f}")
