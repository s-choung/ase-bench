from ase import Atoms
from ase.build import bulk
from ase.neighborlist import natural_cutoffs, NeighborList

# Build Cu FCC supercell
atoms = bulk('Cu', 'fcc', a=3.61)
atoms = atoms * (3, 3, 3)

# Build neighbor list with natural cutoffs
cutoffs = natural_cutoffs(atoms)
nl = NeighborList(cutoffs, skin=0.0, self_interaction=False, bothways=True)

# Update neighbor list
nl.update(atoms)

# Count neighbors for each atom
n_neighbors = [len(nl.get_neighbors(i)[0]) for i in range(len(atoms))]

# Print average coordination number
print(f"Average coordination number: {sum(n_neighbors) / len(n_neighbors):.2f}")
