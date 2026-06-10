from ase.build import fcc111, molecule
from ase.visualize import view

slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)
co = molecule('CO')
co.center(vacuum=0, axis=2)
co.translate([0, 0, 2.0])
slab.extend(co)
print(len(slab))
