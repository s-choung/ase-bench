from ase import Atoms
from ase.build import fcc111, add_adsorbate

slab = fcc111("Pt", size=(2, 2, 4))
co = Atoms("CO", positions=[(0, 0, 0), (0, 0, 1.15)])

add_adsorbate(slab, co, height=1.85, position="ontop", mol_index=0)
slab.center(vacuum=10.0, axis=2)

print(len(slab))
