from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

# Build Cu FCC 3x3x3 supercell
atoms = bulk('Cu', 'fcc', a=3.6).repeat((3, 3, 3))

# Create neighbor list with natural cutoffs
cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, skin=0.0, self_interaction=False, bothways=True)
nl.update_neighbors(atoms)

# Calculate total neighbors and average coordination number
total_neighbors = sum(len(nl.get_neighbors(i)[0]) for i in range(len(atoms)))
avg_coordination = total_neighbors / len(atoms)

print(f'Average coordination number: {avg_coordination:.2f}')
