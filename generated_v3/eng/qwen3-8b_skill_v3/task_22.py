from ase.build import fcc111, add_adsorbate
from ase import molecule

slab = fcc111('Al', size=(1, 1, 3), vacuum=10.0)
add_adsorbate(slab, molecule('N2'), height=2.0, position='bridge')
slab.calc = EMT()
print(len(slab), slab.get_chemical_symbols())
