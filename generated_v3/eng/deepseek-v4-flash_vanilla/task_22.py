import numpy as np
from ase.build import fcc111, molecule
from ase import Atoms

# Create Al(111) slab: 2x2 surface, 3 layers, 10 Å vacuum
slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)

# Create N2 molecule
n2 = molecule('N2')

# Find top layer atoms (largest z)
z_top = np.max(slab.positions[:, 2])
top_mask = np.abs(slab.positions[:, 2] - z_top) < 1e-6
top_indices = np.where(top_mask)[0]
top_positions = slab.positions[top_indices]

# Find a pair of nearest neighbors in top layer
n_top = len(top_indices)
d_min = float('inf')
pair = None
for i in range(n_top):
    for j in range(i+1, n_top):
        d = np.linalg.norm(top_positions[i] - top_positions[j])
        if d < d_min:
            d_min = d
            pair = (i, j)
i1, i2 = pair
midpoint = (top_positions[i1] + top_positions[i2]) / 2

# Place N2 such that its center is at the bridge site, 2.0 Å above top layer
n2.translate([midpoint[0], midpoint[1], z_top + 2.0])

# Combine slab and adsorbate
combined = slab + n2

# Print number of atoms and atom types
print(f"Number of atoms: {len(combined)}")
print(f"Atom types: {set(combined.get_chemical_symbols())}")
