from ase.build import fcc111, molecule, add_adsorbate
from ase import units
from ase.calculators.emt import EMT

slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')
slab.calc = EMT()
print(len(slab))
