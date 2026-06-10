from ase import Atoms
from ase.build import fcc111, molecule, add_adsorbate

slab = fcc111('Al', size=(2, 2, 3))
add_adsorbate(slab, molecule('N2'), 2.0, 'bridge')
slab.center(vacuum=10, axis=2)

print(len(slab))
print(slab.get_chemical_symbols())
print(set(slab.get_chemical_symbols()))
print(len(set(slab.get_chemical_symbols())))
