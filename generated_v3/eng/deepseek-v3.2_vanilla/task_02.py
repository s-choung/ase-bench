from ase.build import fcc111, add_adsorbate
from ase.visualize import view

slab = fcc111('Pt', size=(1, 1, 4), vacuum=10.0)
add_adsorbate(slab, 'CO', height=1.5, position='ontop')

print(len(slab))
