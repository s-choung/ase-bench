from ase import Atoms
from ase.build import fcc111, add_adsorbate

slab = fcc111("Pt", size=(2, 2, 4), vacuum=None)
co = Atoms("CO", positions=[(0, 0, 0), (0, 0, 1.15)])

add_adsorbate(slab, co, height=1.85, position="ontop")
slab.center(vacuum=10.0, axis=2)

print(len(slab))
