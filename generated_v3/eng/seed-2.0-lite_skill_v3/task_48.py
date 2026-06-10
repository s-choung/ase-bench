from ase.build import bulk
from ase.geometry import get_distances

# Create 2x2x2 supercell of FCC Cu bulk
atoms = bulk('Cu', 'fcc', a=3.6).repeat((2, 2, 2))

# Calculate PBC-corrected distances from atom 0 to all other atoms
_, dists = get_distances(
    atoms.positions[0:1], atoms.positions[1:],
    cell=atoms.cell, pbc=atoms.pbc, mic=True
)

# Print min and max distances
print(f"Minimum distance: {dists.min():.3f} Å")
print(f"Maximum distance: {dists.max():.3f} Å")
