from ase import Atoms
from ase.build import fcc111, add_adsorbate

slab = fcc111('Pt', size=(2, 2, 4), vacuum=10)
CO = Atoms('CO', positions=[[0, 0, 0], [0, 0, 1.2]])
add_adsorbate(slab, CO, 2.0, 'ontop')
print(len(slab))
