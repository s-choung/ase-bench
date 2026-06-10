from ase import Atoms
from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
import numpy as np

# Pt(111) slab: 3 layers, 2x2 surface cell, 10 Å vacuum
slab = fcc111('Pt', size=(2,2,3), vacuum=10.0)

# OH adsorbate
oh = molecule('OH')

# Determine top layer Pt atoms
pos = slab.get_positions()
z_top = pos[:,2].max()
top_mask = pos[:,2] > z_top - 0.5          # select atoms in the top layer
top_scaled = slab.get_scaled_positions()[top_mask]

# Ontop site: above the first top atom
ontop_frac = top_scaled[0][:2]             # fractional (x,y)

# Bridge site: midpoint of two nearest-neighbor top atoms
top_cart = pos[top_mask]
dist = np.linalg.norm(top_cart[:,None,:2] - top_cart[None,:,:2], axis=2)
np.fill_diagonal(dist, np.inf)             # ignore self‑distance
i, j = np.unravel_index(np.argmin(dist), dist.shape)
bridge_frac = (slab.get_scaled_positions()[top_mask][i][:2] +
               slab.get_scaled_positions()[top_mask][j][:2]) / 2.0

# FCC hollow site: (1/3, 2/3) of the surface unit cell
hollow_frac = np.array([1./3., 2./3.])

height = 1.0  # Å above the surface

energies = {}
for name, frac in [('ontop', ontop_frac), ('bridge', bridge_frac), ('fcc_hollow', hollow_frac)]:
    slab_copy = slab.copy()
    add_adsorbate(slab_copy, oh, height=height, position=frac)
    slab_copy.calc = EMT()
    e = slab_copy.get_potential_energy()
    energies[name] = e
    print(f'{name}: {e:.3f} eV')

lowest_site = min(energies, key=energies.get)
print(f'\nLowest energy site: {lowest_site} ({energies[lowest_site]:.3f} eV)')
