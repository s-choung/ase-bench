from ase.build import fcc111, molecule
import numpy as np

# Build 3‑layer Al(111) slab with 10 Å vacuum
slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)

# Identify top‑layer atoms
z_vals = slab.positions[:, 2]
top_z = np.max(z_vals)
top_mask = np.abs(z_vals - top_z) < 1e-6
top_indices = np.where(top_mask)[0]
top_pos = slab.positions[top_indices]

# Find two nearest‑neighbour top atoms for the bridge site
dist_xy = np.linalg.norm(top_pos[:, None, :2] - top_pos[None, :, :2], axis=-1)
np.fill_diagonal(dist_xy, np.inf)
i, j = np.unravel_index(np.argmin(dist_xy), dist_xy.shape)
pos1, pos2 = top_pos[i], top_pos[j]

bridge_xy = (pos1[:2] + pos2[:2]) / 2.0
bridge_z  = top_z + 2.0                      # height = 2.0 Å above the surface

# Prepare N₂ molecule, oriented along the bridge direction
n2 = molecule('N2')
bond_len = n2.get_distance(0, 1)
direction = pos2[:2] - pos1[:2]
direction /= np.linalg.norm(direction)
dir3 = np.array([direction[0], direction[1], 0.0])
center = np.array([bridge_xy[0], bridge_xy[1], bridge_z])
n2.positions[0] = center + 0.5 * bond_len * dir3
n2.positions[1] = center - 0.5 * bond_len * dir3

# Combine slab and adsorbate
system = slab + n2

# Output requested information
print("Number of atoms:", len(system))
symbols = system.get_chemical_symbols()
unique, counts = np.unique(symbols, return_counts=True)
print("Atom types:", dict(zip(unique, counts)))
