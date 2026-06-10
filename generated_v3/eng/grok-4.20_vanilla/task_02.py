from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.io import write

slab = fcc111('Pt', size=(4, 4, 4), vacuum=10.0)
add_adsorbate(slab, 'CO', height=2.0, position=(0, 0), offset=(0.5, 0.5))

print(len(slab))
