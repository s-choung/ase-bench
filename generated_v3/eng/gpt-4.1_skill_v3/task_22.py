from ase.build import fcc111, molecule, add_adsorbate
from ase.constraints import FixAtoms
import numpy as np

# Create Al(111) slab: 3x3 surface (default) with 3 layers, 10 Å vacuum
slab = fcc111('Al', size=(3, 3, 3), vacuum=10.0)

# Get N2 molecule
n2 = molecule('N2')

# Bridge site: midpoint between two nearest neighbor Al atoms on the top layer
top_layer = slab.positions[:,2].max()
inds = np.where(np.abs(slab.positions[:,2] - top_layer) < 1e-3)[0]
i, j = inds[:2]
pos_bridge = 0.5*(slab.positions[i][:2] + slab.positions[j][:2])

# Add N2 on bridge site, height from slab
add_adsorbate(slab, n2, height=2.0, position=pos_bridge)

# Print requested info
symbols = slab.get_chemical_symbols()
print('Number of atoms:', len(slab))
print('Atom types:', sorted(set(symbols)))
