#!/usr/bin/env python
# Minimal ASE script: Al(111) 3‑layer slab + N₂ adsorbed on a bridge site

from ase.build import fcc111, add_adsorbate, molecule
from ase.visualize import view  # optional, not used for I/O

# 1. Al(111) slab, 2×2 surface, 3 layers, 10 Å vacuum
slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)

# 2. N₂ molecule
n2 = molecule('N2')

# 3. Adsorb N₂ on the bridge site, 2.0 Å above the surface
add_adsorbate(slab, n2, height=2.0, position='bridge')  # in‑place modification

# 4. Report atom count and element types
num_atoms = len(slab)
elem_types = sorted(set(slab.get_chemical_symbols()))

print(f'Number of atoms: {num_atoms}')
print('Element types:', ', '.join(elem_types))
