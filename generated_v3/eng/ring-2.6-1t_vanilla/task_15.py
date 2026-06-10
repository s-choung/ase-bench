from ase.build import fcc100
from ase.calculators.emt import EMT

# Build Cu(100) slab: 3×3 in‑plane repeats, 3 layers, 12 Å vacuum
slab = fcc100('Cu', size=(3, 3, 3), vacuum=12.0)
slab.calc = EMT()                     # attach a built‑in EMT calculator

# Output
print('Number of atoms:', len(slab))
print('Cell:')
print(slab.cell)
