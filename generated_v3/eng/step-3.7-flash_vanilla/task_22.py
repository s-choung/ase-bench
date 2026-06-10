from ase.build import surface, molecule, add_adsorbate
from ase.calculators.emt import EMT

slab = surface('Al', (1, 1, 1), layers=3, size=(2, 1, 1))
add_adsorbate(slab, molecule('N2'), height=2.0, position='bridge')
slab.center(vacuum=10, axis=2)
slab.calc = EMT()
print(len(slab))
print(sorted(set(slab.get_chemical_symbols())))
