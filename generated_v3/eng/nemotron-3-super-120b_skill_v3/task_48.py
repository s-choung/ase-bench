from ase.build import bulk
from ase.geometry import get_distances

# Create Cu FCC bulk and make a 2x2x2 supercell
cu = bulk('Cu', 'fcc', a=3.6)          # lattice constant approx. 3.6 Å
supercell = cu * (2, 2, 2)            # or cu.repeat((2, 2, 2))

# Compute distances from atom 0 to all atoms, applying minimum image convention
all_indices = list(range(len(supercell)))
distances = get_distances([0], all_indices,
                          cell=supercell.get_cell(),
                          pbc=supercell.get_pbc(),
                          mic=True)[0]   # shape (N,)

# Exclude the self-distance (zero)
other_distances = distances[1:]

min_dist = other_distances.min()
max_dist = other_distances.max()

print(f"Minimum distance from atom 0 to any other atom: {min_dist:.4f} Å")
print(f"Maximum distance from atom 0 to any other atom: {max_dist:.4f} Å")
