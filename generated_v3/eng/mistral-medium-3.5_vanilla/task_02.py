from ase.build import fcc111, molecule
from ase import Atoms

slab = fcc111('Pt', (4, 4, 4), vacuum=10)
co = molecule('CO')
co.position[2] += 2.0
slab += co
print(len(slab))
