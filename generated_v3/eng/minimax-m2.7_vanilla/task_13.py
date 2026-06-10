from ase.build import bulk

# Primitive diamond‑cubic cell of Si
cell = bulk('Si', 'diamond', a=5.43)

# 3×3×3 supercell
scell = cell * (3, 3, 3)

print('Number of atoms:', len(scell))
print('Cell volume (Å^3):', scell.get_volume())
