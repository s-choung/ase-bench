from ase.build import bulk
from ase.neighborlist import NeighborList

# Create Cu FCC unit cell and repeat to 3x3x3 supercell
atoms = bulk('Cu', 'fcc', a=3.615, cubic=True).repeat((3, 3, 3))

# Build neighbor list with natural cutoffs
nl = NeighborList(natural_cutoffs=True, bothways=True, self_interaction=False)
nl.update(atoms)

# Count neighbors per atom
num_neighbors = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]
avg_coord = sum(num_neighbors) / len(atoms)

print(f"Average coordination number: {avg_coord:.3f}")
