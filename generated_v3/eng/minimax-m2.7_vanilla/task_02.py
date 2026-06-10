from ase.build import fcc111, add_vacuum
from ase import Atoms

# Pt(111) slab – 4 layers, (1×1) surface cell
slab = fcc111('Pt', size=(1, 1, 4))

# Identify the topmost Pt atom for the ontop site
top_idx = slab.positions[:, 2].argmax()
top_pos = slab[top_idx].position

# CO molecule: C binds to the surface, O above C (vertical orientation)
co = Atoms('CO')
co[0].position = top_pos + (0, 0, 1.8)      # C 1.8 Å above the surface
co[1].position = co[0].position + (0, 0, 1.15)  # O at C–O bond length (~1.15 Å)
slab.extend(co)

# Add 10 Å of vacuum in the z‑direction
add_vacuum(slab, 10)

print(len(slab))
