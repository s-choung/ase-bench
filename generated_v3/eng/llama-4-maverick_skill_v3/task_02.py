from ase import Atoms
from ase.build import fcc111, molecule, add_adsorbate, add_vacuum

slab = fcc111('Pt', size=(2,2,4), vacuum=0)
co = molecule('CO')
add_adsorbate(slab, co, height=1.8, position='ontop')
add_vacuum(slab, 10)

print(len(slab))
