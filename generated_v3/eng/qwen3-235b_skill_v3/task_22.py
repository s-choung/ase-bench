from ase.build import fcc111, add_adsorbate, molecule
from ase import Atoms

slab = fcc111('Al', size=(1,1,3), vacuum=10)
n2 = molecule('N2')
add_adsorbate(slab, n2, height=2.0, position='bridge')

print(len(slab))
print(slab.get_atomic_numbers())
