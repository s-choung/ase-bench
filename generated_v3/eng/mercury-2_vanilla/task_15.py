from ase.build import surface
from ase.calculators.emt import EMT

# Cu(100) slab, 3 atomic layers, 12 Å vacuum
slab = surface('Cu', (1, 0, 0), layers=3, vacuum=12.0)

# 3×3×3 supercell
slab = slab.repeat((3, 3, 3))

# optional calculator (built‑in)
slab.set_calculator(EMT())

print('Number of atoms:', len(slab))
print('Cell vectors (Å):')
print(slab.get_cell())
