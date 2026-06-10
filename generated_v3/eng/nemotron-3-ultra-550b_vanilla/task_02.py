from ase.build import fcc111, add_adsorbate, molecule
from ase import Atoms

# Create Pt(111) slab: 4 layers, 2x2 surface unit cell
slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)

# Create CO molecule
co = molecule('CO')

# Adsorb CO on ontop site (position (0,0) in surface unit cell)
# Height ~1.8-2.0 Å typical for Pt-CO ontop; use 1.85 Å
add_adsorbate(slab, co, height=1.85, position=(0, 0))

print(len(slab))
