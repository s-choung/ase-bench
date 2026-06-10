from ase.build import fcc111
from ase import Atoms
import numpy as np

# Lattice constant for Pt (angstrom)
a = 3.924

# Create 4-layer Pt(111) slab with 10 Å vacuum
slab = fcc111('Pt', a=a, size=(2, 2, 4), vacuum=10.0)

# Find topmost Pt atom (largest z coordinate)
z_top = slab.positions[:, 2].max()

# CO molecule: C at origin, O along z-axis
co = Atoms('CO', positions=[[0, 0, 0], [0, 0, 1.15]])

# Place C above the top Pt atom at a height of 2.0 Å (ontop site)
# Find the Pt atom with maximum z, get its x,y
idx = np.argmax(slab.positions[:, 2])
x_top, y_top = slab.positions[idx, 0], slab.positions[idx, 1]
co.translate([x_top, y_top, z_top + 2.0])

# Combine slab and adsorbate
system = slab + co

print(len(system))
