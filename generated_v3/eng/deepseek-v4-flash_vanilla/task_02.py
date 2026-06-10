from ase.build import fcc111, add_adsorbate, molecule
from ase import Atoms

# Create Pt(111) 4-layer slab with 10 Å vacuum
slab = fcc111('Pt', size=(1, 1, 4), vacuum=10.0)

# Pick a surface atom (first atom after sort by z descending)
surface_xy = slab.positions[slab.positions[:, 2].argmax(), :2]

# Create CO molecule: C at origin, O at 1.15 Å along z
co = molecule('CO')
co.rotate(180, 'x')  # rotate so C points down (C lowest z)

# Adsorb CO on top site with C–Pt distance 1.85 Å
add_adsorbate(slab, co, height=1.85, position=surface_xy)

# Reset vacuum to 10 Å above topmost atom (including CO)
slab.center(vacuum=10.0, axis=2)

print('Number of atoms:', len(slab))
