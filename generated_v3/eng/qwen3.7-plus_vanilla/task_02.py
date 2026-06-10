from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT

slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)
add_adsorbate(slab, 'CO', height=1.5, position='ontop')
slab.calc = EMT()
print(len(slab))
