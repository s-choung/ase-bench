from ase.build import surface, molecule, add_adsorbate
from ase.calculators.emt import EMT

slab = surface('Pt', (1, 1, 1), layers=4, vacuum=10.0)
co = molecule('CO')
add_adsorbate(slab, co, height=1.5, position='ontop')

slab.calc = EMT()
print(len(slab))
