from ase.build import surface
from ase import Atoms

slab = surface('Pt', (1, 1, 1), 4, vacuum=10.0)
top_pos = max(slab.positions, key=lambda p: p[2])
co = Atoms('CO', positions=[
    (top_pos[0], top_pos[1], top_pos[2] + 1.85),
    (top_pos[0], top_pos[1], top_pos[2] + 2.98)])
slab.extend(co)
print(len(slab))
