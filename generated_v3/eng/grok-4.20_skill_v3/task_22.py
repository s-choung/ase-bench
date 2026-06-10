from ase.build import fcc111, molecule, add_adsorbate
from ase import Atoms
from ase.calculators.emt import EMT

slab = fcc111('Al', size=(3,3,3), vacuum=10.0)
n2 = molecule('N2')
add_adsorbate(slab, n2, height=2.0, position='bridge')
slab.calc = EMT()
print(len(slab))
print(slab.get_chemical_formula())
