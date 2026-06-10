from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

# Create 3x3x3 FCC Cu supercell
atoms = bulk('Cu', 'fcc', a=3.61).repeat((3, 3, 3))

# Build neighbor list with natural element-specific cutoffs
cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, bothways=True)
nl.update(atoms)

# Calculate coordination number for each atom
coordination = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]
avg_cn = sum(coordination) / len(coordination)

print(f"Average coordination number: {avg_cn:.2f}")
