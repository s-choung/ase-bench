from ase import Atoms
from ase.build import fcc111, add_adsorbate, molecule
from ase.calculators.emt import EMT
import numpy as np

# ---------- 3‑layer Pt(111) slab ----------
slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)
slab.center(axis=2, vacuum=10.0)

# indices of the top‑most layer (highest z)
z = slab.get_positions()[:, 2]
top_idx = np.argsort(z)[-9:]          # 3×3 surface layer

# ---------- OH molecule ----------
oh = molecule('OH')
oh.translate(-oh.get_center_of_mass())   # centre at origin

height = 2.0                              # adsorption height (Å)

# ---------- helper to attach OH and return energy ----------
def energy(slab, pos):
    s = slab.copy()
    add_adsorbate(s, oh, height, pos)
    s.calc = EMT()
    return s.get_potential_energy()

# ----- on‑top site (above first surface atom) -----
p_top = slab.get_positions()[top_idx[0], :2]
e_top = energy(slab, p_top)

# ----- bridge site (mid‑point of two neighbouring atoms) -----
p_a = slab.get_positions()[top_idx[0], :2]
p_b = slab.get_positions()[top_idx[1], :2]
p_bridge = (p_a + p_b) / 2.0
e_bridge = energy(slab, p_bridge)

# ----- fcc hollow site (centre of three surface atoms) -----
p_tri = np.mean([slab.get_positions()[i, :2] for i in top_idx[:3]], axis=0)
e_hollow = energy(slab, p_tri)

# ----- compare -----
sites = {'ontop': e_top, 'bridge': e_bridge, 'fcc_hollow': e_hollow}
best = min(sites, key=sites.get)

print('Energies (eV):')
for site, e in sites.items():
    print(f'  {site:>12s}: {e:.4f}')
print(f'\nMost stable site: {best}')
