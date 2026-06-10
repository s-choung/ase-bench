from ase.build import fcc111, molecule, add_adsorbate
from collections import Counter

# 3‑layer Al(111) slab with 10 Å vacuum (2×2 surface cell)
slab = fcc111('Al', size=(2, 2, 3), vacuum=10.0)

# N₂ molecule from ASE database
n2 = molecule('N2')

# Adsorb on a bridge site at 2.0 Å height
add_adsorbate(slab, n2, height=2.0, position='bridge')

# Information
print('Number of atoms:', len(slab))
print('Atom types:', dict(Counter(slab.get_chemical_symbols())))
