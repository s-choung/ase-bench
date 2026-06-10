from ase import Atoms
from ase.build import bulk
from ase.geometry import get_distances

# Create Cu FCC bulk 2x2x2 supercell
atoms = bulk('Cu', 'fcc', a=3.6).repeat((2, 2, 2))

# Get distances from atom 0 to all others (pbc-aware)
indices = range(len(atoms))
dists, _ = get_distances(atoms.positions, [atoms.positions[0]] * len(atoms),  # or just `[atoms[0].position]` but keeping structure
                         cell=atoms.cell, pbc=atoms.pbc, mic=True)
dists = dists[0]  # Extract the distances from the first row

# Alternatively, a clearer way:
# dist_matrix, _ = get_distances(atoms.positions, cell=atoms.cell, pbc=atoms.pbc, mic=True)
# dists = dist_matrix[0]  # Distances from atom 0 to all others

# Filter out self-distance (which is 0) by taking dists[1:] but keeping all for min/max is fine as 0 will be min
print(f"Minimum distance: {min(dists):.4f} Å")
print(f"Maximum distance: {max(dists):.4f} Å")

# If you want to avoid the self-distance (though min will be 0 anyway), you can do:
nonzero_dists = [d for d in dists if d > 1e-8]  # Skip near-zero (self) distance
if nonzero_dists:
    print(f"Minimum (non-zero) distance: {min(nonzero_dists):.4f} Å")
