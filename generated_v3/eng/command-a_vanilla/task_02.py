from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT

# Create Pt(111) 4-layer slab with 10 Å vacuum
slab = fcc111('Pt', size=(2, 2, 4), vacuum=10.0)

# Add CO molecule to the ontop site
add_adsorbate(slab, 'CO', height=1.8, position='ontop')

# Attach EMT calculator
slab.calc = EMT()

# Print number of atoms
print(len(slab))
