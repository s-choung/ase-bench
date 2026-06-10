from ase.build import fcc111, add_adsorbate
from ase import Atoms

slab = fcc111('Pt', size=(1, 1, 4), vacuum=10.0)
co = Atoms('CO', positions=[(0, 0, 0), (0, 0, 1.14)])
add_adsorbate(slab, co, height=2.0, position='ontop')

print(len(slab))
