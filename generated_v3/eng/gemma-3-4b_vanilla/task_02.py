from ase import Atoms
from ase.build import fcc111, add_adsorbate

slab = fcc111('Pt', size=(4, 4, 4), shift=2)
slab.vacuum = 10.0

add_adsorbate(slab, 'CO', height=2.0, position='ontop')

print(len(slab.atoms))
