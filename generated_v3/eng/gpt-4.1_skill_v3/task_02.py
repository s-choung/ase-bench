from ase.build import fcc111, molecule, add_adsorbate
from ase import Atoms

slab = fcc111('Pt', size=(1,1,4), vacuum=10.0)
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')
print(len(slab))
