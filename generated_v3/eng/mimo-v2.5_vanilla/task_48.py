from ase.build import bulk
from ase import Atoms

# Build Cu FCC bulk and create 2x2x2 supercell
cu_bulk = bulk('Cu', 'fcc', a=3.615, cubic=True)
cu_supercell = cu_bulk * (2, 2, 2)

# Calculate distances from atom 0 to all other atoms with periodic boundaries
distances = cu_supercell.get_distances(0, range(len(cu_supercell)), mic=True)

# Print minimum and maximum distances
print(f"Min distance: {distances.min():.4f} Å")
print(f"Max distance: {distances.max():.4f} Å")
