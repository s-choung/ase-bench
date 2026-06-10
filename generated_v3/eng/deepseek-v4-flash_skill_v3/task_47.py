from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

# Build Cu FCC 3x3x3 supercell
atoms = bulk('Cu', 'fcc', a=3.615) * (3, 3, 3)

# Construct neighbor list with natural cutoffs
cutoffs = natural_cutoffs(atoms, mult=1.0)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

# Count neighbors per atom
neighbor_counts = []
for i in range(len(atoms)):
    indices, offsets = nl.get_neighbors(i)
    neighbor_counts.append(len(indices))

avg_coordination = sum(neighbor_counts) / len(atoms)
print(f"Average coordination number: {avg_coordination:.2f}")
