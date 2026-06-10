import numpy as np
from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

# Build 3x3x3 Cu FCC supercell
atoms = bulk('Cu', 'fcc', a=3.6).repeat((3, 3, 3))

# Get natural cutoffs for all atoms
cutoffs = natural_cutoffs(atoms)

# Create NeighborList using natural cutoffs (using a small tolerance for robustness)
# We iterate through atoms to get their specific cutoff
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

# Calculate coordination numbers
# nl.get_neighbors() returns indices of neighbors for each atom
coordination_numbers = [len(nl.get_neighbors(i)) for i in range(len(atoms))]

avg_cn = np.mean(coordination_numbers)
print(f"Average Coordination Number: {avg_cn:.2f}")
