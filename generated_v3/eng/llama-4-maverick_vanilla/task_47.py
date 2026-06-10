from ase import Atoms
from ase.neighborlist import NeighborList, natural_cutoffs

# Create a Cu FCC 3x3x3 supercell
cu = Atoms('Cu', positions=[[0, 0, 0]], cell=[[3.6, 0, 0], [0, 3.6, 0], [0, 0, 3.6]], pbc=True)
cu *= (3, 3, 3)

# Build a NeighborList
cutoffs = natural_cutoffs(cu)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(cu)

# Calculate the number of neighbors for each atom and print the average coordination number
coordination_numbers = [len(nl.get_neighbors(i)[0]) for i in range(len(cu))]
print(sum(coordination_numbers) / len(cu))
