from ase.build import fcc111, add_adsorbate
from ase import Atoms

# Create a 4-layer Pt(111) slab with 3x3 surface unit cell
slab = fcc111('Pt', size=(3, 3, 4), vacuum=10.0)

# Create CO molecule
co = Atoms('CO', positions=[[0, 0, 0], [0, 0, 1.15]])

# Add CO on top of the first Pt atom (ontop site)
add_adsorbate(slab, co, height=1.8, position=(0, 0))

print(len(slab))
