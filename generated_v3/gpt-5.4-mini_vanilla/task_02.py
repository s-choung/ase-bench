from ase.build import fcc111, molecule
from ase.io import write

slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)
co = molecule('CO')
co.rotate(90, 'y', rotate_cell=False)

site = slab[0].position.copy()
co.translate(site - co[0].position + [0, 0, 1.85])

system = slab + co
print(len(system))
