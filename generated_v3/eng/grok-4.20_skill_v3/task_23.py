from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
import numpy as np

slab = fcc111('Pt', size=(4,4,3), vacuum=10.0)
oh = molecule('OH')

# ontop
s1 = slab.copy()
add_adsorbate(s1, oh, 1.8, 'ontop')
s1.calc = EMT()
e1 = s1.get_potential_energy()

# bridge
s2 = slab.copy()
add_adsorbate(s2, oh, 1.6, 'bridge')
s2.calc = EMT()
e2 = s2.get_potential_energy()

# fcc hollow
s3 = slab.copy()
add_adsorbate(s3, oh, 1.5, 'fcc')
s3.calc = EMT()
e3 = s3.get_potential_energy()

energies = {'ontop': e1, 'bridge': e2, 'fcc': e3}
lowest = min(energies, key=energies.get)

print('Ontop energy:', e1)
print('Bridge energy:', e2)
print('FCC energy:', e3)
print('Lowest energy site:', lowest)
