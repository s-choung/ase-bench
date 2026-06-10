from ase.build import bulk
from ase.neighborlist import natural_cutoffs, NeighborList

# Create Cu FCC bulk and repeat to 3x3x3 supercell
atoms = bulk('Cu', 'fcc', a=3.615, cubic=True)
atoms = atoms.repeat((3, 3, 3))

# Get natural cutoffs for the system
cutoffs = natural_cutoffs(atoms)

# Build neighbor list (no self‑interaction, count each pair both ways)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

# Number of neighbors for each atom
neighbor_counts = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]
avg_coordination = sum(neighbor_counts) / len(atoms)

print(f'Average coordination number: {avg_coordination:.3f}')
