from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

# Build Cu FCC 3x3x3 supercell
atoms = bulk('Cu', 'fcc', a=3.6) * (3, 3, 3)

# Neighbor list using natural cutoffs
cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, self_interaction=False, bothways=True)
nl.update(atoms)

# Coordination numbers
coords = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]
avg_coord = sum(coords) / len(atoms)

print(f"Average coordination number: {avg_coord:.2f}")
