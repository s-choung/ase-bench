from ase.build import fcc111, add_adsorbate, molecule
from collections import Counter
import numpy as np

slab = fcc111('Al', size=(1, 1, 3), vacuum=10.0)
n2 = molecule('N2')
add_adsorbate(slab, n2, height=2.0, position='bridge')

print(f"Number of atoms: {len(slab)}")
counts = Counter(slab.get_chemical_symbols())
for sym, cnt in counts.items():
    print(f"  {sym}: {cnt}")
