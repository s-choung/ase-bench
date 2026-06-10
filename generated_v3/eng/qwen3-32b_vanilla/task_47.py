from ase.build import fcc
from ase import neighborlist

# Create Cu FCC 3x3x3 supercell
atoms = fcc('Cu', size=(3, 3, 3), latticeconstant=3.615)

# Generate neighbor list with natural cutoffs
cutoffs = neighborlist.natural_cutoffs(atoms)
nl = neighborlist.NeighborList(cutoffs, self_reject=True, bothways=True)
nl.update(atoms)

# Calculate coordination numbers
total = 0
for i in range(len(atoms)):
    neighbors, _ = nl.get_neighbors(i)
    total += len(neighbors)

# Output average coordination number
print(f"Average coordination number: {total / len(atoms):.2f}")
