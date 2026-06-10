from ase.build import bulk, surface

# BCC Fe bulk (lattice constant ≈2.86 Å)
fe_bulk = bulk('Fe', 'bcc', a=2.86)

# (110) surface, 4 atomic layers, 10 Å vacuum
slab = surface(fe_bulk, (1, 1, 0), layers=4, vacuum=10.0)

# 2×2 in‑plane supercell (size = (2,2,4) → 2×2 repeats, 4 layers already set)
slab = slab.repeat((2, 2, 1))

print("Number of atoms :", len(slab))
print("Cell vectors (Å):\n", slab.get_cell())
