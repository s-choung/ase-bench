import numpy as np
from ase.build import fcc111, add_adsorbate
from ase import Atoms
from ase.calculators.emt import EMT

# Pt lattice constant
a = 3.92

# 3‑layer 3×3 slab with vacuum
slab = fcc111('Pt', size=(3, 3, 3), a=a, vacuum=10.0)

# Identify top‑most layer atoms (highest z)
zmax = slab.positions[:, 2].max()
top_layer_idx = [i for i, z in enumerate(slab.positions[:, 2]) if abs(z - zmax) < 0.1]

# Reference atom and its two nearest neighbours in the top layer
ref_idx = top_layer_idx[0]
dists = slab.get_distances(ref_idx, top_layer_idx)
order = np.argsort(dists)
nn1_idx = top_layer_idx[order[1]]
nn2_idx = top_layer_idx[order[2]]

ref = slab.positions[ref_idx]
nn1 = slab.positions[nn1_idx]
nn2 = slab.positions[nn2_idx]

# Adsorbate sites (x, y)
top_site = ref[:2]
bridge_site = (ref[:2] + nn1[:2]) / 2
fcc_site = (ref[:2] + nn1[:2] + nn2[:2]) / 3

# OH molecule (O at origin, H along z)
oh = Atoms('OH', positions=[(0, 0, 0), (0, 0, 0.98)])
height = 1.5  # O‑surface distance

# Build three structures and attach EMT calculator
structures = {}
for name, pos in [('top', top_site), ('bridge', bridge_site), ('fcc', fcc_site)]:
    s = slab.copy()
    add_adsorbate(s, oh, height, pos)
    s.calc = EMT()
    structures[name] = s

# Single‑point energies
energies = {name: s.get_potential_energy() for name, s in structures.items()}

# Output
for name, e in energies.items():
    print(f'{name}: {e:.4f} eV')
min_site = min(energies, key=energies.get)
print(f'Lowest energy site: {min_site} ({energies[min_site]:.4f} eV)')
