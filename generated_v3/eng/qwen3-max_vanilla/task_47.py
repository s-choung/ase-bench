from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

# Create Cu FCC 3x3x3 supercell
cu = bulk('Cu', 'fcc', a=3.6)
cu *= (3, 3, 3)

# Build neighbor list using natural cutoffs
cutoffs = natural_cutoffs(cu)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(cu)

# Count neighbors for each atom
coord_nums = []
for i in range(len(cu)):
    indices, _ = nl.get_neighbors(i)
    coord_nums.append(len(indices))

# Print average coordination number
avg_coord = sum(coord_nums) / len(coord_nums)
print(f'Average coordination number: {avg_coord:.2f}')
