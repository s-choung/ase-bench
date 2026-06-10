from ase import Atoms
from ase.build import bulk
from ase.neighborlist import NeighborList, natural_cutoffs

# Create FCC Cu bulk and 3x3x3 supercell
cu = bulk('Cu', 'fcc', a=3.615, cubic=True)
supercell = cu * (3, 3, 3)

# Get natural cutoffs and build NeighborList
cutoffs = natural_cutoffs(cu)
nl = NeighborList(cutoffs, bothways=True)
nl.update(supercell)

# Calculate coordination numbers for each atom
n_atoms = len(supercell)
coord_numbers = [len(nl.get_neighbors(i)[0]) for i in range(n_atoms)]

# Print results
print(f"Total atoms: {n_atoms}")
print(f"Total bonds: {sum(coord_numbers) // 2}")
print(f"Average coordination number: {sum(coord_numbers) / n_atoms:.2f}")
