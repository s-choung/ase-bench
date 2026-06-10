from ase.build import fcc111, add_adsorbate, molecule
from ase.calculators.emt import EMT

slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)
add_adsorbate(slab, molecule('CO'), 1.8, 'ontop')
slab.calc = EMT()
print(len(slab))
