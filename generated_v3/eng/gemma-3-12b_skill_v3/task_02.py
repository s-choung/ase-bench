from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT

slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)
co = Atoms('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')

print(len(slab))
