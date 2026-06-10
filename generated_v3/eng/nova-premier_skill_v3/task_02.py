from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT

slab = fcc111('Pt', (2,2,4), vacuum=10)
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')
slab.calc = EMT()
print(len(slab))
