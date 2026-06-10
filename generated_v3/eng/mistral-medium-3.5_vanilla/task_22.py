from ase.build import molecule, fcc111, add_adsorbate
from ase import Atoms

slab = fcc111('Al', (1, 1, 1), layers=3, vacuum=10)
n2 = molecule('N2')
add_adsorbate(slab, n2, height=2.0, position=(0.5, 0.5))
print(len(slab), set(slab.get_chemical_symbols()))
