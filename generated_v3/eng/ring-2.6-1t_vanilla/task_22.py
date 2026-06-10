from ase import Atoms
from ase.build import fcc111, molecule
from collections import Counter
import numpy as np

# Al(111) slab, 3 layers, 2×2 surface repeat, 10 Å vacuum
slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0, orthogonal=True)
slab.pbc = [True, True, False]

# N₂ molecule (bond along z)
n2 = molecule('N2')

# Find topmost layer
z_max = slab.positions[:, 2].max()
top_mask = slab.positions[:, 2] > z_max - 0.5
top_pos = slab.positions[top_mask]

# Mid‑point of two adjacent top‑layer atoms (bridge site)
p1, p2 = top_pos[0, :2], top_pos[1, :2]
mid_xy = (p1 + p2) / 2.0

# Desired height of N₂ centre above the slab top
height = 2.0
z_center = z_max + height

# Translate N₂ so its centre of mass lies at the bridge site
n2.translate(np.array([mid_xy[0], mid_xy[1], z_center]) - n2.get_center_of_mass())

# Combine slab and molecule
system = slab + n2

# Output
print('Total atoms:', len(system))
print('Atom types:', dict(Counter(system.get_chemical_symbols())))
