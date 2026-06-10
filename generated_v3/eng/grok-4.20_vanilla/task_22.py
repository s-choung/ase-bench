from ase.build import fcc111, molecule, add_adsorbate
from ase.constraints import FixAtoms
import numpy as np

slab = fcc111('Al', size=(3, 3, 3), vacuum=10.0)
n2 = molecule('N2')

add_adsorbate(slab, n2, height=2.0, position='bridge')

print(len(slab))
print(np.unique(slab.get_chemical_symbols()))
