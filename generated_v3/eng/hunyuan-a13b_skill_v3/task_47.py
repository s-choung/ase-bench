from ase import Atoms
from ase.neighborlist import NeighborList, natural_cutoffs

# Build Cu FCC 3x3x3 supercell
atoms = Atoms('Cu', 'fcc', a=3.6, cellwidths=(3.6, 3.6, 3.6))
atoms_pbc = atoms * (3, 3, 3)  # Repeat to 3x3x3 supercell

# Create NeighborList
cutoff = natural_cutoffs(atoms_pbc, pbc=True)
nl = NeighborList(cutoff, pbc=True)
nl.build()

# Initialize and count neighbors
counts = [0] * len(atoms_pbc)
for i, neighbors in enumerate(nl):
    counts[i] = len(neighbors)

# Calculate and print average coordination number
avg_coordination = sum(counts) / len(atoms_pbc)
print(avg_coordination)
