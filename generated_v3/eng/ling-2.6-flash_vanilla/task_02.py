from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.constraints import FixAtoms

slab = fcc111('Pt', size=(1, 4, 4), vacuum=10.0)
add_adsorbate(slab, 'CO', (0, 0), 'ontop')
slab.set_constraint(FixAtoms(mask=slab.positions[:, 2] < 5.0))
print(len(slab))
