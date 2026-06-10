from ase.build import bulk
from ase.neighborlist import NeighborList
import numpy as np

# Create Cu FCC 3x3x3 supercell
atoms = bulk('Cu', 'fcc', a=3.61) * (3, 3, 3)

# Build neighbor list using natural cutoffs
nl = NeighborList(natural_cutoffs=True, self_interaction=False, bothways=True)
nl.update(atoms)

# Coordination number for each atom
coord = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]

# Average
avg = np.mean(coord)
print(f"Average coordination number: {avg:.3f}")
