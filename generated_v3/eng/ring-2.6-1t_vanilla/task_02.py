from ase.build import fcc111, molecule
from ase import Atoms

# 4‑layer Pt(111) slab with 10 Å vacuum on both sides
slab = fcc111('Pt', size=(3, 3, 4), vacuum=10.0)

# position of the highest (surface) atom
top_idx = slab.positions[:, 2].argmax()
top_pos = slab.positions[top_idx]

# CO molecule, oriented vertically
co = molecule('CO')

# place the C atom ~1.9 Å above the on‑top site (typical Pt–C distance)
shift = top_pos + [0, 0, 1.9] - co.positions[0]
co.translate(shift)

# attach CO to the slab
slab.extend(co)

print(len(slab))
