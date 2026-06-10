from ase.build import fcc111, molecule, add_adsorbate, add_vacuum
from ase import Atoms

slab = fcc111('Al', (3,3,3), vacuum=0, periodic=True)
add_vacuum(slab, 10)
n2 = molecule('N2')
add_adsorbate(slab, n2, 2.0, 'bridge')

print(len(slab), sorted({a.symbol for a in slab}))
