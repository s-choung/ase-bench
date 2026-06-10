from ase.build import fcc111, add_adsorbate
from ase.build import molecule

slab = fcc111('Al', size=(2,2,3), vacuum=10.0)
n2 = molecule('N2')
add_adsorbate(slab, n2, height=2.0, position='bridge')

print("Number of atoms:", len(slab))
print("Chemical symbols:", slab.get_chemical_symbols())
print("Chemical formula:", slab.get_chemical_formula())
