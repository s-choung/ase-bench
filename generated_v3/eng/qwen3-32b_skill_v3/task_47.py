from ase import bulk
from ase.neighborlist import natural_cutoffs, NeighborList

# Create 3x3x3 Cu FCC supercell
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (3, 3, 3)

# Build neighbor list with natural cutoffs
cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, skin=0.0, self=False)
nl.update(atoms)

# Calculate coordination numbers
nneighbors = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]
avg_coordination = sum(nneighbors) / len(atoms)

print(f"Average coordination number: {avg_coordination:.2f}")
