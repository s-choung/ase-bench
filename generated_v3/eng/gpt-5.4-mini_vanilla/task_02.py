from ase.build import fcc111, molecule
from ase.constraints import FixAtoms
from ase.io import write

slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)
co = molecule('CO')
co.rotate(90, 'y', rotate_cell=False)

slab += co
slab[-2].position = slab[0].position + (0, 0, 1.85)
slab[-1].position = slab[-2].position + (0, 0, 1.15)

print(len(slab))
