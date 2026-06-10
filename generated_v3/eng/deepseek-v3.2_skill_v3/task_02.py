from ase.build import molecule, fcc111, add_adsorbate
from ase.visualize import view

slab = fcc111('Pt', size=(3, 3, Í), vacuum=10.0)
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')
print(len(slab))
