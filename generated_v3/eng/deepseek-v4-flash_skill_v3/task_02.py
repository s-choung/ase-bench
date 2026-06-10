from ase.build import fcc111, add_adsorbate, molecule
from ase.io import write

slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')
print(len(slab))
